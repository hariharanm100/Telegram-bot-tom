import stripe

stripe.api_key = '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'
products = stripe.Product.list()
print(products)
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Your Product Name',
                        },
                        'unit_amount': 2000,  # Amount in cents (e.g., $20.00)
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://yourdomain.com/success',  # Redirect after successful payment
            cancel_url='https://yourdomain.com/cancel',  # Redirect if payment is canceled
        )   
        print('Checkout session created:', session.id)
        return session.id
    except stripe.error.StripeError as e:
        print('Error creating checkout session:', e)
        raise e


def generate_payment_link(session_id):
    try:
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        payment_link = checkout_session.url
        print('Payment link:', payment_link)
        return payment_link
    except stripe.error.StripeError as e:
        print('Error generating payment link:', e)
        raise e

# Call the function to create a checkout session
s = create_checkout_session()
# Generate payment link using the session ID
payment_link = generate_payment_link(s)

def check_payment_status(session_id):
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        payment_status = session.payment_status
        print('Payment status:', payment_status)
        return payment_status
    except stripe.error.StripeError as e:
        print('Error retrieving payment status:', e)
        raise e

# Provide the session ID for which you want to check the payment status


# Check the payment status for the given session ID
payment_status = check_payment_status(s)


# Verify payment status using session ID
def verify_payment_status(session_id):
    intents = stripe.PaymentIntent.list()
    for intent in intents.auto_paging_iter():
        if intent.metadata.get('session_id') == session_id:
            return intent.status
    return None  # Session ID not found or payment not associated
