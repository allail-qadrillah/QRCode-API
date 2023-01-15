import uvicorn
from fastapi import FastAPI, HTTPException, Response
import qrcode
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.get("/")
async def create_qr_code(url: str):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        return Response(content=buffer.read(), media_type='image/png', headers={"Content-Disposition": "attachment; filename=qrcode.png"})
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error generating QR code")

@app.get('/api')
def alwaysOnReplit():
  return "online"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)