from pathlib import Path
from io import BytesIO
import qrcode


def generate_qr(data, file_name):
    path = Path("/tmp/Your QR Codes")
    path.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)

    img_path = path / file_name
    img = qr.make_image()
    img.save(img_path)

    return img_path


def generate_qr_bytes(data):
    """Generate a QR code and return it as raw PNG bytes."""
    qr = qrcode.QRCode(
        box_size=12,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer.getvalue()
