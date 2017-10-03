from pyquery import PyQuery as pq
import requests as req



resp = req.get("https://www.autotrader.co.za/used-cars/hyundai/h-1/2016-hyundai-h-1-2.5crdi-wagon-gls-fpa-8a81c85d5d2bbac0015d2c914c2f2c0e")
doc = pq(resp.text)

classspan = doc("div.spec-value").text()
print(classspan)
print '------------------------------'
classprice = doc("div.price").text()
print(classprice)
print '------------------------------'
print("Make Specific")
for row in doc("div.accordion-body div.alternating-bg"):
    if pq(row).find("div.spec-name").text() == "Make":
        print pq(row).find("div.spec-value").text()
  
print '------------------------------'
print("Model Specific")
for row in doc("div.accordion-body div.alternating-bg"):
    if pq(row).find("div.spec-name").text() == "Model":
        print pq(row).find("div.spec-value").text()
