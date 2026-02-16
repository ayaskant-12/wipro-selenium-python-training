from flask import Flask, request, jsonify

app = Flask(__name__)

# -----------------------------
# Fake Database
# -----------------------------

doctors = {}
patients = {}
appointments = {}

doctor_counter = 500
patient_counter = 100
appointment_counter = 1000

cancelled_appointments = set()

# -----------------------------
# Doctor Creation
# -----------------------------

@app.route("/v1/doctors", methods=["POST"])
def create_doctor():

    global doctor_counter

    data = request.get_json()

    doctor_counter += 1

    doctor = {
        "doctor_id": doctor_counter,
        "name": data.get("name"),
        "specialization": data.get("specialization"),
        "experience": data.get("experience")
    }

    doctors[doctor_counter] = doctor

    return jsonify(doctor), 201


# -----------------------------
# Patient Registration
# -----------------------------

@app.route("/v1/patients", methods=["POST"])
def create_patient():


    global patient_counter

    data = request.get_json()

    age = data.get("age")
    email = data.get("email")
    phone = data.get("phone")

    # Validation

    if age is None or age < 0:
        return jsonify({"error": "Invalid age"}), 400

    if not email:
        return jsonify({"error": "Email required"}), 400

    # Duplicate phone check

    for p in patients.values():
        if p["phone"] == phone:
            return jsonify({"error": "Phone already exists"}), 409

    patient_counter += 1

    patient = {
        "patient_id": patient_counter,
        "name": data.get("name"),
        "age": age,
        "email": email,
        "phone": phone
    }

    patients[patient_counter] = patient

    return jsonify(patient), 201


# -----------------------------
# Book Appointment
# -----------------------------

@app.route("/v1/appointments", methods=["POST"])
def book_appointment():


    global appointment_counter

    data = request.get_json()

    patient_id = data.get("patient_id")
    doctor_id = data.get("doctor_id")
    date = data.get("date")
    time = data.get("time")

    # Check if slot already booked

    for appt in appointments.values():
        if appt["doctor_id"] == doctor_id and appt["date"] == date and appt["time"] == time:
            return jsonify({"error": "Slot already booked"}), 409

    appointment_counter += 1

    appointment = {
        "appointment_id": appointment_counter,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time
    }

    appointments[appointment_counter] = appointment

    return jsonify(appointment), 201


# -----------------------------
# View Appointment
# -----------------------------

@app.route("/v1/appointments/<int:id>", methods=["GET"])
def view_appointment(id):


    if id in appointments:
        return jsonify(appointments[id]), 200

    if id in cancelled_appointments:
        return jsonify({"error": "Appointment cancelled"}), 410

    return jsonify({"error": "Not found"}), 404


# -----------------------------
# Reschedule Appointment
# -----------------------------

@app.route("/v1/appointments/<int:id>", methods=["PUT"])
def reschedule(id):


    if id not in appointments:
        return jsonify({"error": "Not found"}), 404

    data = request.get_json()

    new_date = data.get("date")
    new_time = data.get("time")

    doctor_id = appointments[id]["doctor_id"]

    # Check conflict

    for appt_id, appt in appointments.items():

        if appt_id != id and appt["doctor_id"] == doctor_id and appt["date"] == new_date and appt["time"] == new_time:
            return jsonify({"error": "Slot already booked"}), 409

    # Update

    appointments[id]["date"] = new_date
    appointments[id]["time"] = new_time

    return jsonify(appointments[id]), 200


# -----------------------------
# Cancel Appointment
# -----------------------------

@app.route("/v1/appointments/<int:id>", methods=["DELETE"])
def cancel(id):


    if id in cancelled_appointments:
        return jsonify({"error": "Already cancelled"}), 410

    if id not in appointments:
        return jsonify({"error": "Not found"}), 404

    cancelled_appointments.add(id)

    del appointments[id]

    return "", 204


# -----------------------------
# Run Server
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)