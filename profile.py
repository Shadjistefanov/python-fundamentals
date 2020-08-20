length_hall = float(input())
width_hall = float(input())
square_side = float(input())
total_area = length_hall * width_hall * 10000
total_square = square_side * square_side * 10000
bench_size = total_area / 10
free_area = total_area - total_square - bench_size
dancers = free_area / 7040
