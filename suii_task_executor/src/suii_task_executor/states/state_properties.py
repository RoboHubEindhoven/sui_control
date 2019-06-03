#! /usr/bin/env python
from enum import Enum

# class StateName(Enum):
#     TASKSELECT = "task_select_state"
#     TASKSELECTNAVIGATION = "navigation_state"
#     GRASP      = "grasp_state"
#     PLACE      = "place_state"
#     EMERGENCY  = "emergency_state"
#     ERROR      = "error_state"

# class TransitionName(Enum):
#     TASKSELECT = "to_task_select_state"
#     NAVIGATION = "to_navigation_state"
#     GRASP      = "to_grasp_state"
#     PLACE      = "to_place_state"
#     EMERGENCY  = "to_emergency_state"
#     ERROR      = "to_error_state"

class StateName(Enum):
    IDLE_STATE      = "idle_state"
    TASK_SELECT     = "task_select_state"
    TASK_EXECUTION  = "task_execution_state"
    EMERGENCY       = "emergency_state"
    ERROR           = "error_state"

class TransitionName(Enum):
    IDLE_STATE      = "to_idle_state"
    TASK_SELECT     = "to_task_select_state"
    TASK_EXECUTION  = "to_task_execution_state"
    EMERGENCY       = "to_emergency_state"
    ERROR           = "to_error_state"