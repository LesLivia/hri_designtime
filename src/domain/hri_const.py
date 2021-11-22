from enum import Enum


class Constants(Enum):
    # Template File Names
    MAIN_TPLT = "main"
    ROB_TPLT = "ROB"
    BTR_TPLT = "BTR"
    HA_TPLT = "HA"
    HC_TPLT = "HC"
    HF_TPLT = "HF"
    HL_TPLT = "HL"
    HRec_TPLT = "HRec"
    HRes_TPLT = "HRes"
    ORCH_TPLT = "ORCH"
    OPCHK_TPLT = "OPCHK"
    ROS_TPLT = "ROS"
    # Keywords to replace templates within main file
    ROB_KEY = "**ROBOT**"
    BTR_KEY = "**BATTERY**"
    HA_KEY = "**HUMAN_ASSISTANT**"
    HC_KEY = "**HUMAN_COMPETITOR**"
    HF_KEY = "**HUMAN_FOLLOWER**"
    HL_KEY = "**HUMAN_LEADER**"
    HRec_KEY = "**HUMAN_RECIPIENT**"
    HRes_KEY = "**HUMAN_RESCUER**"
    ORCH_KEY = "**ORCHESTRATOR**"
    OPCHK_KEY = "**OPCHK**"
    ROS_KEY = "**ROS**"
    # Keywords to replace params within main file
    # Human-related params
    N_H = "**N_H**"
    N_H_bool = "**N_H_false**"
    N_H_double = "**N_H_0.0**"
    N_H_int = "**N_H_0**"
    PATTERNS = "**PTRNS**"
    START_X = "**START_X**"
    START_Y = "**START_Y**"
    DEST_X = "**DEST_X**"
    DEST_Y = "**DEST_Y**"
    SAME_IDs_MAT = "**SAME_IDs_MAT**"
    #
    TAU = "**TAU**"
    # Layout-related params
    N_AREAS = "**N_A**"
    N_POINTS = "**N_P**"
    N_P_double = "**N_P_0.0**"
    N_INTERSECT = "**N_I**"
    N_I_false = "**N_I_false**"
    MAX_NEIGH = "**max_neigh**"
    MAX_NEIGH_int = "**max_neigh_-1**"
    LAYOUT = "**LAYOUT**"
    INTERSECT = "**INTERSECTIONS**"
    # Instances-related params
    ROB_INST = "**ROB_INST**"
    ORCH_INST = "**ORCH_INST**"
    HUM_INST = "**HUM_INST**"
    ALL_INST = "**ALL_INST**"
