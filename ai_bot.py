customers = {}

# ---------------- LOAD COMPANY INFO ----------------
def load_company_info():
    try:
        with open("company_info.txt", "r", encoding="utf-8") as file:
            return file.read()
    except:
        return ""

company_info = load_company_info()


# ---------------- GET SECTION ----------------
def get_section(title):
    text = company_info

    start = text.upper().find(title.upper())
    if start == -1:
        return "Information not available."

    remaining = text[start + len(title):]
    lines = remaining.split("\n")

    result = []

    for line in lines:
        clean = line.strip()

        if clean.endswith(":") and clean.isupper():
            break

        if clean:
            result.append(clean)

    return f"{title}\n" + "\n".join(result)


# ---------------- MAIN BOT ----------------
def ask_ai(customer_id, message):

    msg = message.lower().strip()

    # ---------------- NEW CUSTOMER ----------------
    if customer_id not in customers:
        customers[customer_id] = {
            "step": "start",
            "name": "",
            "location": "",
            "purpose": ""
        }

        return "Hi 👋 Welcome to XXX Solar Company ☀️ How can I help you today?"

    customer = customers[customer_id]

    # ---------------- CONVERSATION FLOW ----------------
    if customer["step"] == "start":
        customer["step"] = "name"
        return "May I know your name?"

    if customer["step"] == "name":
        customer["name"] = message
        customer["step"] = "location"
        return f"Nice to meet you {message} 😊 May I know your location?"

    if customer["step"] == "location":
        customer["location"] = message
        customer["step"] = "purpose"
        return "Home, Office, or Industry solar requirement?"

    if customer["step"] == "purpose":
        customer["purpose"] = message
        customer["step"] = "chat"
        return "Thanks ☀️ How can I help you further?"

    # ---------------- COMPANY INFO (HIGH PRIORITY) ----------------

    # PRODUCT
    if any(x in msg for x in ["product", "products", "solar product", "show product"]):
        return get_section("OUR SOLAR PRODUCTS & SOLUTIONS")

    # SERVICE
    if "service" in msg or "services" in msg:
        return get_section("SERVICES")

    # BENEFIT
    if "benefit" in msg:
        return get_section("BENEFITS OF SOLAR ENERGY")

    # ABOUT
    if "about" in msg:
        return get_section("ABOUT COMPANY")

    # VISION
    if "vision" in msg:
        return get_section("VISION")

    # MISSION
    if "mission" in msg:
        return get_section("MISSION")

    # INSTALLATION
    if "installation" in msg or "process" in msg:
        return get_section("INSTALLATION PROCESS")

    # SUPPORT
    if "support" in msg:
        return get_section("CUSTOMER SUPPORT")

    # CONTACT
    if "contact" in msg:
        return get_section("CONTACT DETAILS")

    # LOCATION
    if "location" in msg:
        return get_section("LOCATION")

    # ---------------- SALES INTENT ----------------
    if any(x in msg for x in ["buy", "purchase", "quotation", "price", "order"]):
        return "Thank you for your interest ☀️ I will connect you with our Sales Manager."

    # ---------------- DEFAULT ----------------
    return (
        "I can help you with:\n"
        "☀️ Products\n"
        "☀️ Services\n"
        "☀️ Installation\n"
        "☀️ Contact details\n"
        "☀️ Solar information"
    )