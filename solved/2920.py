pitch = ['1', '2', '3', '4', '5', '6', '7', '8']
revPitch = list(reversed(pitch))

inputPitch = list(input().split())

if pitch == inputPitch:
    print('ascending')
elif revPitch == inputPitch:
    print('descending')
else:
    print('mixed')
