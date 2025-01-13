//
//  main.swift
//  Algorithm
//
//  Created by 윤재형 on 1/14/25.
//

import Foundation

var num = readLine()!.split(separator: " ").map{ Int(String($0))!}
//var str = readLine()!

print( (num[0] + num[1]) % num[2])
print( ((num[0] % num[2]) + (num[1] % num[2])) % num[2])
print( (num[0] * num[1]) % num[2])
print( ((num[0] % num[2]) * (num[1]%num[2]))%num[2])
