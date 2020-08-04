import abc
import random

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

    # undo  too lazy to write


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.high()


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.off()


class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.open()


class GarageDoorCloseCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.close()


class StereoOnForCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()


class DancingModeOn(Command):
    def __init__(self, dancing_mode):
        self.dancing_mode = dancing_mode

    def execute(self):
        self.dancing_mode.on()


class DancingModeOff(Command):
    def __init__(self, dancing_mode):
        self.dancing_mode = dancing_mode

    def execute(self):
        self.dancing_mode.off()


class OnOffThing:
    def on(self):
        print('{} light is on'.format(self.name))

    def off(self):
        print('{} light is off'.format(self.name))


class Light(OnOffThing):
    def __init__(self, name='light'):
        self.name = name


class CeilingFan:
    def __init__(self, name='fan'):
        self.name = name

    def high(self):
        print('{} is high'.format(self.name))

    def off(self):
        print('{} is off'.format(self.name))


class GarageDoor:
    def __init__(self, name='garage door'):
        self.name = name

    def open(self):
        print('{} is open'.format(self.name))

    def close(self):
        print('{} is close'.format(self.name))


class Stereo(OnOffThing):
    def __init__(self, name='stereo'):
        self.name = name


class DancingMode(OnOffThing):
    def __init__(self, name='dancing mode'):
        self.name = name


class RemoteControl:
    def __init__(self, on_commands, off_commands):
        self.on_commands = on_commands
        self.off_commands = off_commands

    def press_on_button(self, idx):
        self.on_commands[idx].execute()

    def press_off_button(self, idx):
        self.off_commands[idx].execute()


llight = Light('living room light')
clight = Light('kitchen light')
ceiling_fan = CeilingFan()
garage_door = GarageDoor()
stereo = Stereo()
all_light = Light('all light')
dancing_mode = DancingMode()

on_commands = []
on_commands.append(LightOnCommand(llight))
on_commands.append(LightOnCommand(clight))
on_commands.append(CeilingFanHighCommand(ceiling_fan))
on_commands.append(GarageDoorOpenCommand(garage_door))
on_commands.append(StereoOnForCDCommand(stereo))
on_commands.append(LightOnCommand(all_light))
on_commands.append(DancingModeOn(dancing_mode))


off_commands = []
off_commands.append(LightOffCommand(llight))
off_commands.append(LightOffCommand(clight))
off_commands.append(CeilingFanOffCommand(ceiling_fan))
off_commands.append(GarageDoorCloseCommand(garage_door))
off_commands.append(StereoOffCommand(stereo))
off_commands.append(LightOffCommand(all_light))
off_commands.append(DancingModeOff(dancing_mode))

remote_control = RemoteControl(on_commands,off_commands)

test_times = 10

for i in range(test_times):
    on_or_off = random.randint(0,1)
    conmmand_idx = random.randint(0,6)
    if on_or_off:
        print('press on {}'.format(conmmand_idx))
        remote_control.press_on_button(conmmand_idx)
    else:
        print('press off {}'.format(conmmand_idx))
        remote_control.press_off_button(conmmand_idx)