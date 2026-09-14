import qrcode

# Paytm payment URL format
# Replace 'YOUR_MERCHANT_ID', 'YOUR_ORDER_ID', 'YOUR_AMOUNT', and 'YOUR_CURRENCY' with actual values
merchant_id = 'YOUR_MERCHANT_ID'
order_id = 'YOUR_ORDER_ID'
amount = 'YOUR_AMOUNT'
currency = 'INR'  # Assuming the currency is Indian Rupee

# Create the Paytm payment link
paytm_payment_link = f'PAYTM:{merchant_id}|{order_id}|{amount}|{currency}'

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(paytm_payment_link)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("paytm_qr_code.png")

print("Paytm QR code generated and saved as paytm_qr_code.png")