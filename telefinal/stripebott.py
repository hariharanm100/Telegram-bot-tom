import stripe

stripe.api_key = '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'
products = stripe.Product.list()
product_id = 'prod_P7H4Th8sU1FmKE'
# print(products)prod_P7H4TpiBSH88sz
# for product in products:
#     print(f"Product ID: {product.id}, Product Name: {product.name}")
# prices = stripe.Price.list(product=product_id)
# for price in prices:
#     print(f"Price ID: {price.id}, Product ID: {price.product}")

# # Create a price for the product
# price = stripe.Price.create(
#     product=product_id,
#     # unit_amount=1000,  # Replace with the actual price amount in cents
#     currency='usd',
# )
# price_id = prices.data[0].id  
# # Create a checkout session using the created price
# session = stripe.checkout.Session.create(
#     payment_method_types=['card'],
#     line_items=[
#         {
#             'price': price_id,  # Use the ID of the created price
#             'quantity': 1,
#         },
#     ],
#     mode='payment',
#     success_url='https://yourwebsite.com/success',
#     cancel_url='https://yourwebsite.com/cancel',
# )

# print(session.url)

# Create a checkout session
# checkout_session = stripe.checkout.Session.create(
#     payment_method_types=['card'],
#     line_items=[
#         {
#             'price': product_id,  # Use the product ID here
#             'quantity': 1,
#         },
#     ],
#     mode='payment',
#     success_url='https://yourwebsite.com/success',
#     cancel_url='https://yourwebsite.com/cancel',
# )

# # Retrieve the URL for the checkout session
# payment_link = checkout_session.url

# print("Payment link:", payment_link)