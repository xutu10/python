book = {'dad':'bob','mom':'lisa'}
print(book)
print(book['mom'])

another = book.copy()
book.clear() # remove all

print another.has_key('dad')
