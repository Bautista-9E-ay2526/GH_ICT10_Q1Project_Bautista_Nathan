from pyscript import display, document


def generate_pizza_sku(e):
    document.getElementById('output_sku').innerHTML = " "
    
    cat_type = document.getElementById('food_type').value
    item_title = document.getElementById('item_name').value
    inventory_val = document.getElementById('stock_amount').value

    generated_sku = cat_type[:3].upper() + "-" + item_title[:4].upper() + "-" + str(inventory_val)

    display("SKU Code: ", generated_sku, target='output_sku')


def create_order(e):
    wings_item = document.getElementById("chicken")
    pasta_item = document.getElementById("spaghetti")
    pizza_item = document.getElementById("pizza")
    tea_item = document.getElementById("iced_tea")
    coca_item = document.getElementById("cola")

    subtotal_cost = (
        float(wings_item.value) * wings_item.checked + 
        float(pasta_item.value) * pasta_item.checked + 
        float(pizza_item.value) * pizza_item.checked + 
        float(tea_item.value) * tea_item.checked + 
        float(coca_item.value) * coca_item.checked
    )

    sales_tax_rate = 0.12
    tax_amount = subtotal_cost * sales_tax_rate
    final_total = subtotal_cost + tax_amount

    receipt_details = f"""
    <div class="receipt-box">
        <h4 class="receipt-header mb-3">==== Receipt ====</h4>
        <p class="mb-1">Subtotal: ₱{subtotal_cost:.2f}</p>
        <p class="mb-1">Tax (12%): ₱{tax_amount:.2f}</p>
        <hr class="my-2">
        <p class="receipt-total mb-0">Total: ₱{final_total:.2f}</p>
    </div>
    """

    document.getElementById("show_receipt").innerHTML = receipt_details