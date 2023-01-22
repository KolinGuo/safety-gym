import safety_gym.envs.suite

import os
import mujoco_py
if 'libGLEW.so' in os.environ.get('LD_PRELOAD', ''):  # using GLFW for viewer
    # https://github.com/openai/mujoco-py/issues/390#issuecomment-525385434
    mujoco_py.GlfwContext(offscreen=True, quiet=True)  # Create a window to init GLFW
