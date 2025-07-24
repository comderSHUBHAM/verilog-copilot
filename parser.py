def detect_simple_errors(verilog_code):
    errors = {}
    corrections = {}
    lines = verilog_code.splitlines()
    for idx, line in enumerate(lines, 1):
        if "initial" in line:
            errors[idx] = "Non-synthesizable: initial block used."
            corrections[idx] = "REMOVE this line for synthesis"
        if "$display" in line:
            errors[idx] = "Non-synthesizable: $display used."
            corrections[idx] = "REMOVE this line for synthesis"
    return errors, corrections
