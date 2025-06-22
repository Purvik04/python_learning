# dictionaries and set

# keys can be string , int, float, bool, tuple

info = {
    "name" : "Purvik",
    "age": 28,
    "is_adult": True
}

null_dict = {}

print(info)
print(info.keys()) #return list of keys 
print(info.values()) #return list of values
print(info.items()) #return list of key-value pairs, each pair in a tuple

print(info["age"]) # error if key not present
print(info.get("age")) #returns none if key not present

info.update({"city": "surat"}) #add new dict inside old dict


# sets in python
# sets are mutable but it's elements are immutable
# unordered , unique and immutable
# list and dict can't be stored in set bcz they are mutable  

set1 = {1,2,3,4,"hello","world","world"}

null_set = set()

print(set1)

set1.add(5)
set1.remove(2)
# set1.remove(7) #if ele not present then error

print(set1.union({3,4,5,6}))
print(set1.intersection({3,4,5,6}))
print(set1.difference({3,4,5,6}))