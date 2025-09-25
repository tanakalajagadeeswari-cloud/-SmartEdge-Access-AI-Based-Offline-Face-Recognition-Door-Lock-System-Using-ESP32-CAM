# SmartEdge Access: Face Recognition Simulation

import random

# --- Mock Database for Stored Faces ---
database = {
    "person_1": [0.1, 0.2, 0.3, 0.4, 0.5],  # Mock feature vector
    "person_2": [0.6, 0.7, 0.8, 0.9, 1.0],  # Mock feature vector
}

# --- Mock Functions for Simulation ---

def capture_image():
    """Simulates capturing an image from the camera."""
    print("\n[SIM] Capturing image...")
    # In a real scenario, this would interface with the camera
    return "mock_image_data"

def detect_face(image):
    """Simulates detecting a face in the image."""
    print("[SIM] Detecting face in the image...")
    # In a real scenario, this would use a face detection model (e.g., MTCNN)
    if random.random() > 0.1:  # 90% chance of detecting a face
        print("[SIM] Face detected.")
        return "mock_face_data"
    else:
        print("[SIM] No face detected.")
        return None

def extract_features(face):
    """Simulates extracting features from the detected face."""
    print("[SIM] Extracting features from the face...")
    # In a real scenario, this would use a face recognition model to get a feature vector
    return [random.uniform(0, 1) for _ in range(5)]

def recognize_face(features):
    """Simulates recognizing the face by comparing features with the database."""
    print("[SIM] Recognizing face...")
    for name, stored_features in database.items():
        # Simulate feature matching (e.g., calculating Euclidean distance)
        distance = sum([(a - b) ** 2 for a, b in zip(features, stored_features)]) ** 0.5
        print(f"[SIM] Comparing with {name}, distance: {distance:.4f}")
        if distance < 0.5:  # Mock threshold for recognition
            print(f"[SIM] Face recognized as {name}.")
            return name
    print("[SIM] Face not recognized.")
    return None

def enroll_new_face(name, features):
    """Simulates enrolling a new face by adding it to the database."""
    print(f"[SIM] Enrolling new face: {name}")
    database[name] = features
    print(f"[SIM] {name} enrolled successfully.")

def unlock_door():
    """Simulates unlocking the door."""
    print("\n[ACTION] Door Unlocked!")

def lock_door():
    """Simulates locking the door."""
    print("\n[ACTION] Door Locked!")

# --- Simulation Workflow ---

def run_simulation():
    """Runs the complete face recognition and door lock simulation."""
    print("--- SmartEdge Access Simulation ---")

    # --- Scenario 1: Recognize an existing user ---
    print("\n--- Scenario 1: Recognizing an existing user ---")
    image = capture_image()
    face = detect_face(image)
    if face:
        # Simulate recognizing an existing person
        features = [0.12, 0.22, 0.32, 0.42, 0.52] # Close to person_1
        print(f"[SIM] Extracted features: {[f\"{x:.2f}\" for x in features]}")
        person = recognize_face(features)
        if person:
            unlock_door()
        else:
            lock_door()

    # --- Scenario 2: Attempt to recognize an unknown user ---
    print("\n--- Scenario 2: Attempting to recognize an unknown user ---")
    image = capture_image()
    face = detect_face(image)
    if face:
        features = extract_features(face) # Random features
        print(f"[SIM] Extracted features: {[f\"{x:.2f}\" for x in features]}")
        person = recognize_face(features)
        if person:
            unlock_door()
        else:
            lock_door()

    # --- Scenario 3: Enroll a new user ---
    print("\n--- Scenario 3: Enrolling a new user ---")
    new_person_name = "person_3"
    image = capture_image()
    face = detect_face(image)
    if face:
        features = extract_features(face)
        print(f"[SIM] Extracted features for enrollment: {[f\"{x:.2f}\" for x in features]}")
        enroll_new_face(new_person_name, features)
        print(f"\n[SIM] Database after enrollment: {database}")

if __name__ == "__main__":
    run_simulation()


