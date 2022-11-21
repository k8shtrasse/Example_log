# SPECIFICATION
# We have to run each definition separate. Instead we will have error.

import re
handle = open("example_log.log")


def counter_ip():
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ipadrs = []
    count = 0
    for element in handle:
        divide_element = element.split(" - - ")
        element1 = divide_element[0]
        ipadrs.append(element1)
    num = ipadrs[0]
    for i in ipadrs:
        curr_value = ipadrs.count(i)
        if curr_value > count:
            count = curr_value
            num = i
    return num


#print(counter_ip())


def most_requested_page():
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    new_list = []
    count = 0
    for elem in handle:
        divide_element = elem.split(" ")
        element = divide_element[10]
        if element == '"-"':
            continue
        new_list.append(element)
    # hum means that we start count the most requested page from zero element in new_list
    hum = new_list[0]
    # new loop for count the most requested page
    for i in new_list:
        value = new_list.count(i)
        if value > count:
            count = value
            hum = i

    return hum


#print(most_requested_page())

#how many requests were there from each ip?


def tasks3():
    # we are creating tuple (requestCount) for store multiple items in single variable
    requestCount = {}
    for line in handle:
        lineParts = line.split(" ")
        ip = lineParts[0]
        link = lineParts[10]
        if link == '"-"':
            continue

        if ip not in requestCount:
            requestCount[ip] = {}

        if link not in requestCount[ip]:
            requestCount[ip][link] = 0

        requestCount[ip][link] += 1

    return requestCount


#print(tasks3())

# what non-existent pages were clients referred to?


def non_existent_pages():
    newlist = []
    for elem in handle:
        divide = elem.split(" ")
        element = divide[10]
        newlist.append(element)
        for none_page in newlist:
            if none_page.startswith('"https'):
                continue
    return none_page


#print(non_existent_pages())


def time_the_most_requests():
    newlist = []
    count = 0
    for element in handle:
        divide = element.split(" ")
        element = divide[3]
        a = element.removeprefix("[25/Apr/2017:")
        newlist.append(a)

    for i in newlist:
        curr_value = newlist.count(i)
        if curr_value > count:
            count = curr_value
            hum = i
    return hum


#print(time_the_most_requests())