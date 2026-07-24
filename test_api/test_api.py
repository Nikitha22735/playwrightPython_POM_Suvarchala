import pytest

from playwright.sync_api import sync_playwright

def getApi(playwright: sync_playwright):
    context = playwright.request.new_context(http_credentials={"username": "admin", "password": "admin"})
    # respBody = context.get("https://dummyjson.com/products", headers={"Authorization":"Bearer 1234567"})
    respBody = context.get("https://dummyjson.com/products")
    print(respBody)
    # print(respBody.json())
    print(respBody.status)
    print(respBody.status_text)
    assert respBody.status==200
    results = respBody.json()
    print(results["products"][0]["title"])



def test_postApi(playwright: sync_playwright):
    context = playwright.request.new_context(http_credentials={"username": "admin", "password": "admin"})
    reqBody ={
        "title": "Gaming Chair",
        "price": 299.99,
        "brand": "DXRacer"
        }
    respBody = context.post("https://dummyjson.com/products/add", data=reqBody)
    print(respBody)
    assert respBody.status==201
    print(respBody.json())