# Import standard python libraries
import os, sys, pytest, json, threading

# Set system path
root_dir = os.environ["OPENAG_BRAIN_ROOT"]
sys.path.append(root_dir)
os.chdir(root_dir)

# Import device utilities
from device.utilities.accessors import get_peripheral_config

# Import mux simulator
from device.comms.i2c2.mux_simulator import MuxSimulator

# Import peripheral driver
from device.peripherals.modules.led_dac5578.driver import LEDDAC5578Driver

# Load test config and setup
base_path = root_dir + "/device/peripherals/modules/led_dac5578/tests/"
device_config = json.load(open(base_path + "config.json"))
peripheral_config = get_peripheral_config(device_config["peripherals"], "LEDPanel-1")
panel_configs = peripheral_config["parameters"]["communication"]["panels"]
peripheral_setup = json.load(open(base_path + "setup.json"))
channel_configs = peripheral_setup["channel_configs"]


def test_init() -> None:
    driver = LEDDAC5578Driver(
        name="Test",
        i2c_lock=threading.RLock(),
        panel_configs=panel_configs,
        channel_configs=channel_configs,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )


def test_turn_on() -> None:
    driver = LEDDAC5578Driver(
        name="Test",
        i2c_lock=threading.RLock(),
        panel_configs=panel_configs,
        channel_configs=channel_configs,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    driver.turn_on()


def test_turn_off() -> None:
    driver = LEDDAC5578Driver(
        name="Test",
        i2c_lock=threading.RLock(),
        panel_configs=panel_configs,
        channel_configs=channel_configs,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    driver.turn_off()


def test_set_spd() -> None:
    driver = LEDDAC5578Driver(
        name="Test",
        i2c_lock=threading.RLock(),
        panel_configs=panel_configs,
        channel_configs=channel_configs,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    distance = 10
    ppfd = 800
    spectrum = {
        "380-399": 0, "400-499": 26, "500-599": 22, "600-700": 39, "701-780": 13
    }
    driver.set_spd(distance, ppfd, spectrum)