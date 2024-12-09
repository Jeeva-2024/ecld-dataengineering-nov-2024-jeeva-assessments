def luke(key):
   dict={'Darth Vader' :'father','leia':'sister','Han':'brother in law','R2D2':'droid'}
   return dict.get(key)
print("luke, i am your",luke('leia'))


