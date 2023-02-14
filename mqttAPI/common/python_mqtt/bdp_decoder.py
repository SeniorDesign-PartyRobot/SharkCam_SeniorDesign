"""Decode bdp data for lidar."""
import json
import os
from enum import Enum
from itertools import islice
from pathlib import Path
from typing import Dict, Union


class BDPExamples(Enum):
    """BDP examples to use if needed."""

    BA = "$BA3E80xxxx5F\r"
    BC = "$BC13E800320\r"
    DA = "$DA640032\r"
    DB = "$DB1320021\r"
    DC = "$DC32xxxx03E8\r"
    DD = "$DD0076C07600032\r"
    DG = "$DG1640032\r"
    DH = "$DH2CCDD\r"
    DJ = "$DJ2CCDDEEFF\r"
    DK = "$DK10000000000001967\r"
    DL = "$DL132002103E8\r"
    DM = "$DM1000640101\r"
    DP = "$DP1\r"
    DR = "$DR000CA\r"
    DS = "$DS1\r"
    DT = "$DT31\r"
    DU = "$DU30001CAAA55\r"
    DV = "$DV4001000000000002D3F000000000000\r"
    DW = "$DW11\r"
    DX = "$DX21\r"
    DY = "$DY0\r"
    EA = "$EA55F0FED0\r"
    EC = "$EC00001111000011112222\r"
    ED = "$ED1\r"
    EP = "$EP0\r"
    LG = "$LG0\r"
    MA = "$MAabcdAABBCCDDHHIIJJKK\r"
    MC = "$MC23\r"
    MD = "$MD1\r"
    ME = "$ME4567\r"
    MF = "$MF0142\r"
    MG = "$MG0258\r"
    MH = "$MH0142\r"
    MM = "$MM111893\r"
    NE = "$NE0111111222223333344444555556666620\r"
    NH = "$NH1\r"
    NI = "$NI10123012301230123012301237FFF\r"
    NP = "$NP0\r"
    NS = "$NS111103\r"
    PD = "$PDje22\r"
    PE = "$PEbindetectdisabled\r"
    PH = "$PHje22\r"
    UI = "$UI01\r"
    WB = "$WBabcdefghijklmnopqrstuvwxyz123456\r"
    WC = "$WC0101A16503Y20A31\r"
    WD = "$WD11111111111000000001101PP1110000\r"
    WE = "$WEx\r"
    WF = "$WF000101May 01 2018"
    WG = "$WG02\r"
    WH = "$WH0001\r"
    WI = "$WI001002367xxx\r"
    WM = "$WM111111111110000000011011111100000000\r"
    WN = "$WN000101May 01 2018"
    WR = "WR00\r"
    WS = "$WSAB123           L101180312H321A0\r"
    WT = "$WT1\r"
    WU = "$WUABCDEFGHIJKLMNO\r"
    WV = "$WVLiIONK91701321A0\r"
    WW = "$WWRV750           L301180302321A0\r"
    WX = "$WXRV750           CY20A3109Z1A7\r"
    WY = "$WYShark_RV18HL-12345ABCDE12\r"
    WZ = "$WZ000101Jan 24 2017\r"


def bdp_decode(data: str, extended: bool = False, append_units: bool = False) -> Dict[str, Union[str, int]]:
    """Decode string value to proper dictionary.

    Args:
        data (str): String version of the BDP Data.
        extended (bool, optional): If whole backend dictionary should be returned. Defaults to False.
        append_units (bool, optional): Append units where applicable. Defaults to False.

    Raises:
        ValueError: If input does not start with $.

    Returns:
        Dict[str, Union[str, int]]: Returns human readable dict.
    """
    with open(os.path.join(Path(__file__).parent, "bdp_defs.json"), "r") as f:
        bdp_defs = json.load(f)
    data = data.replace("\r", "")
    if not data.startswith("$"):
        raise ValueError(f"This is not a proper returned value. {data}")
    data = data[1:]
    decode_query = data[:2]
    decode_values = iter(data[2:])
    query_breakdown = bdp_defs[decode_query]
    query_breakdown_keys = list(query_breakdown.keys())
    splited_chunks = [
        "".join(islice(decode_values, None, x)) for x in map(lambda x: query_breakdown[x]["size"], query_breakdown_keys)
    ]
    for key in query_breakdown:
        query_breakdown_value = splited_chunks[query_breakdown_keys.index(key)]
        if query_breakdown_value == "" or query_breakdown_value[0] in ["x", "_"]:
            if extended:
                query_breakdown[key]["value"] = -1
            else:
                query_breakdown[key] = -1
        elif not query_breakdown[key]["convert"]:
            if query_breakdown[key]["special"]:
                query_breakdown_value = eval(f"{query_breakdown_value}" + query_breakdown[key]["special"])
            if append_units:
                query_breakdown_value = f"{query_breakdown_value}{query_breakdown[key]['unit']}"
            if extended:
                query_breakdown[key]["value"] = query_breakdown_value
            else:
                query_breakdown[key] = query_breakdown_value
        else:
            _val = int(query_breakdown_value, 16)
            if query_breakdown[key]["special"]:
                _val = eval(f"{_val}" + query_breakdown[key]["special"])
            if append_units:
                _val = f"{_val}{query_breakdown[key]['unit']}"
            if extended:
                query_breakdown[key]["value"] = _val
            else:
                query_breakdown[key] = _val
    return query_breakdown
