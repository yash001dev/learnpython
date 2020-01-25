#Dictionary it is based on Key and Value Pair and Each Key Must be Unique
customer={
    "name":"YASH N SANGHAVI",
    "age":19,
    "is_verified":True
}
customer["name"]="MANAN H SANGHAVI"
print(customer["name"])
print(customer.get("birthdate","Jan 1 1980"))
