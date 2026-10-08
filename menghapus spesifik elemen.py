fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
print("fellowship:", fellowship)

fellowship.discard('boromir')
print("fellowship:", fellowship)

fellowship.remove('gandalf')
print("fellowship:", fellowship)
#Perbedaan dua method di atas: jika elemen yang ingin dihapus tidak ada, method discard() tidak memunculkan error, sedangkan method remove() memunculkan error.