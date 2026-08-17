import base64
from flask import Flask, render_template, request, send_file
from io import BytesIO
from qr_generator import generate_qr, generate_qr_bytes

app = Flask(__name__)

# Pre-generate example QR codes at startup
EXAMPLES = [
    {"label": "Website URL", "text": "https://github.com/Harsh031202"},
    {"label": "Plain Text", "text": "Hello! Welcome to my QR Code Generator."},
    {"label": "WiFi Network", "text": "WIFI:T:WPA;S:HomeNetwork;P:mypassword;;"},
    {"label": "Email Address", "text": "mailto:hkharsh3122@gmail.com"},
    {"label": "LinkedIn Profile", "text": "https://linkedin.com/in/harsh-kumar-harsh-dark"},
    {"label": "Phone Number", "text": "tel:+91-9876543210"},
]

for ex in EXAMPLES:
    ex["qr"] = base64.b64encode(generate_qr_bytes(ex["text"])).decode("utf-8")


def _render(**kwargs):
    """Render index.html with examples always injected."""
    return render_template("index.html", examples=EXAMPLES, **kwargs)


@app.route("/")
def index():
    return _render()


@app.route("/generate", methods=["POST"])
def generate():
    data = request.form.get("data", "").strip()
    filename = request.form.get("filename", "").strip()

    if not data:
        return _render(error="Please enter a URL or text.")

    # Generate QR as bytes for display
    qr_bytes = generate_qr_bytes(data)
    qr_b64 = base64.b64encode(qr_bytes).decode("utf-8")

    # Also save to disk using original function
    save_name = (filename if filename else "qrcode") + ".png"
    generate_qr(data, save_name)

    return _render(
        qr_image=qr_b64,
        qr_data=data,
        qr_filename=save_name,
        success=True,
    )


@app.route("/download")
def download():
    data = request.args.get("data", "").strip()
    filename = request.args.get("filename", "qrcode.png")

    if not data:
        return "No data provided", 400

    qr_bytes = generate_qr_bytes(data)
    buffer = BytesIO(qr_bytes)
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="image/png",
        as_attachment=True,
        download_name=filename,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
