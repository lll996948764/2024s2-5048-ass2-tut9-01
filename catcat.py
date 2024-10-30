import numpy as np
from datetime import datetime, timedelta

# Define states
states = ["S1", "S2", "S3", "S4", "S5"]

# Define the transition matrix based on the given probabilities
transition_matrix = {
    "S1": {"S3": 1.0},
    "S2": {"S1": 0.2, "S3": 0.8},
    "S3": {"S2": 0.38, "S4": 0.38, "S5": 0.24},  # Adjust probabilities to sum to 1
    "S4": {"S3": 1.0},
    "S5": {"S2": 1.0}
}

def get_next_state(current_state):
    next_states = list(transition_matrix[current_state].keys())
    probabilities = list(transition_matrix[current_state].values())
    return np.random.choice(next_states, p=probabilities)

def simulate_path(start_state, path, start_timestamp):
    current_state = start_state
    timestamp = start_timestamp
    log_entries = []
    for _ in path:
        next_state = get_next_state(current_state)
        log_entries.append(f"{timestamp.strftime('%d/%b/%Y %H:%M:%S')} | {current_state} -> {next_state}")
        current_state = next_state
        timestamp += timedelta(seconds=1)  # Increment timestamp by 1 second for each transition
    return log_entries

# Define test cases
test_cases = {
    "Test Case 01": ["S1", "S2", "S3", "S4", "S1"],
    "Test Case 02": ["S1", "S2", "S3", "S5", "S1"],
    "Test Case 03": ["S1", "S2", "S3", "S2", "S1"],
    "Test Case 04": ["S1", "S2", "S1"]
}

# Generate a starting timestamp
start_timestamp = datetime.now()

# Collect log entries
all_log_entries = []
for path in test_cases.values():
    all_log_entries.extend(simulate_path("S1", path, start_timestamp))

# Sort log entries by time
all_log_entries.sort()

# Print sorted log entries
for entry in all_log_entries:
    print(entry)
