//
//  main.swift
//  hex2rgb
//
//  Created by Noirdemort on 25/02/19.
//  Copyright © 2019 Noirdemort. All rights reserved.
//

import Foundation
extension String {
    subscript(_ range: CountableRange<Int>) -> String {
        let idx1 = index(startIndex, offsetBy: max(0, range.lowerBound))
        let idx2 = index(startIndex, offsetBy: min(self.count, range.upperBound))
        return String(self[idx1..<idx2])
    }
}

let accepted_values = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

print("\t\t Hex to RGB Convertor!")
while true {
    print("\n Enter hex value or -1 to exit: ")
    var hex = readLine()!

    if hex == "-1" {
        break
    }

    for i in hex {
        if !accepted_values.contains("\(i)") {
            hex = "-2"
        }
    }
 
    if (hex == "-2" || hex.count != 6){
        print("Invalid hex!")
        continue
    }
  
    let convert_red = UInt16(String(hex[0..<2]), radix: 16)!
    let convert_green = UInt16(String(hex[2..<4]), radix: 16)!
    let convert_blue = UInt16(String(hex[4..<6]), radix: 16)!
    print("red: \(convert_red), green: \(convert_green), blue: \(convert_blue)")
    
}

