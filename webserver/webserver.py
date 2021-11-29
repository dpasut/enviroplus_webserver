import time
from subprocess import PIPE, Popen

try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559

    ltr559 = LTR559()
except ImportError:
    import ltr559

from bme280 import BME280
from enviroplus import gas
from flask import Flask
from pms5003 import PMS5003
from pms5003 import ReadTimeoutError as pmsReadTimeoutError
from pms5003 import SerialTimeoutError

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

pms5003 = PMS5003()


def getGas():
    readings = gas.read_all()
    return readings


def getCpuTemp():
    process = Popen(["vcgencmd", "measure_temp"], stdout=PIPE)
    output, _error = process.communicate()
    output = output.decode()
    return float(output[output.index("=") + 1 : output.rindex("'")])


def getTemp():
    # adjust factor for better results, higher factor to increse temp
    factor = 0.8
    rawTemp = bme280.get_temperature()
    cpuTemp = getCpuTemp()
    calcTemp = cpuTemp - (cpuTemp - rawTemp) / factor
    return calcTemp


def getPressure():
    return bme280.get_pressure()


def getHumidity():
    return bme280.get_humidity()


def getLight():
    return ltr559.get_lux()


def getParticles():
    try:
        pms_data = pms5003.read()
    except (SerialTimeoutError, pmsReadTimeoutError):
        return "Failed to read PMS5003."
    else:
        return pms_data.pm_ug_per_m3(1.0), pms_data.pm_ug_per_m3(2.5), pms_data.pm_ug_per_m3(10)


app = Flask(__name__)


@app.route("/")
def main():
    temp = getTemp()
    gas = getGas()
    pressure = getPressure()
    light = getLight()
    humidity = getHumidity()
    particulate = getParticles()
    return """
            <meta http-equiv='refresh' content='1'>
            Welcome to the EnviroPi Webserver!<br/>
            Temperature = {} <br/>
            Gas = {} <br/>
            Pressure = {} <br/>
            Light = {} <br/>
            Humidity = {} <br/>
            Particulate Matter = {} <br/>
        """.format(
        temp, gas, pressure, light, humidity, particulate
    )


@app.route("/debug")
def debug():
    cpuTemp = getCpuTemp()
    rawTemp = bme280.get_temperature()
    temp = getTemp()
    return """
    CPU Temp = {} <br/>
    Raw Temp = {} <br/>
    Temp = {} <br/>
    """.format(
        cpuTemp, rawTemp, temp
    )
