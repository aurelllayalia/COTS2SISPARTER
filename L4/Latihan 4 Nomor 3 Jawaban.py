#Import mpi4py
from mpi4py import MPI

#Import library random untuk generate angka integer secara random
from random import randint

#Membuat COMM
comm = MPI.COMM_WORLD

#Mendapatkan rank proses
rank = comm.Get_rank()

#Mendapatkan total proses berjalan
size = comm.Get_size()

#Generate angka integer secara random untuk setiap proses
generates_number = randint(0,100)

#Jika saya adalah proses dengan rank 0 maka:
#Saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
#Menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
    jumlah = 0
    print('===========================================================================')
    print('Proses untuk rank', rank)
    for higher_rank in range(1, size):
        generates_number = comm.recv(source = higher_rank)
        print('rank', rank, 'menerima nilai', generates_number, 'dari rank', higher_rank)
        jumlah += generates_number
    print('Hasil Penjumlahan = ', jumlah)
	
#Jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    lowest_rank = 0
    comm.send(generates_number, dest = lowest_rank)
    print('===========================================================================')
    print('Proses untuk rank',rank)
    print('rank', rank, 'mengirim nilai', generates_number, 'ke rank', lowest_rank)
