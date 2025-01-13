//
//  main.swift
//  Algorithm
//
//  Created by 윤재형 on 1/14/25.
//

import Foundation

//var num = readLine()!.split(separator: " ").map{ Int(String($0))!}
//var str = readLine()!
var num1 = Int(readLine()!)!
var num2 = readLine()!.map{ Int(String($0))!}
var num3 = String(num2[0]) + String(num2[1]) + String(num2[2])

print(num1 * num2[2])
print(num1 * num2[1])
print(num1 * num2[0])
print(num1*Int(num3)!)
