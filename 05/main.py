import requests
import bs4
import collections

WeatherReport = collections.namedtuple("report", "location, current_temperature, Max_temp, Min_temp, cndtn")


def main():
    print_the_header()
    html = get_html_from_web()

    # parse the html
    report = get_weather_from_html(html)
    print(report)


def print_the_header():
    print("----------------------------------")
    print("\t Weather App")
    print("----------------------------------")


def get_html_from_web():
    url = input("please paste in the url")
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    loc = []
    # location = "_ngcontent-app-root-c192"
    # WeathCondition ="div .class="current-temp""
    soup = bs4.BeautifulSoup(html, 'html.parser')

    loc = soup.h1.find("span").get_text()
    temp = soup.find("div", class_="current-temp").get_text()
    htemp = soup.find("span", class_="hi").get_text()
    ltemp = soup.find("span", class_="lo").get_text()
    wcondition = soup.find("div", class_="condition-icon").get_text()
    # aqi = soup.find(id="aqBarChart")
    cctemp = fahrenheit_to_Cel(temp)
    hctemp = int((int(htemp[0:2])-32)/1.8)
    lctemp = int((int(ltemp[0:2])-32)/1.8)
    # hctemp = fahrenheit_to_Cel(htemp)
    print("Weather Report for today: {}".format(loc))
    # print(temp)
    print("Current Temperature is: {}".format(cctemp))
    # print(htemp)
    print("Hightest Temperature for toay is: {}".format(hctemp), chr(176)+"C")
    print("Lowest Temperature for toady is: {}".format(lctemp), chr(176)+"C")
    print("General Weather Condition is: {}".format(wcondition))
    # print("Air Quality is: {}".format(aqi))
    report = WeatherReport(location=loc, current_temperature=cctemp,
                           Max_temp=hctemp, Min_temp=lctemp, cndtn=wcondition)
    return report


def fahrenheit_to_Cel(fahrenheit: str) -> str:
    ctemp = int(fahrenheit.split()[0])
    ctemp = int((ctemp-32)/1.8)
    pctemp = str(ctemp)+" "+chr(176)+"C"
    return pctemp


if __name__ == "__main__":
    main()
