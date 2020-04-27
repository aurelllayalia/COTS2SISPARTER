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
print('===========================================================================')
print('Proses untuk rank', rank, ', nilai = ', generates_number)

#Melakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
jumlah = comm.allreduce(generates_number, op = MPI.SUM)

#Jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank == 0:
        print('Hasil Penjumlahan = ', jumlah)
