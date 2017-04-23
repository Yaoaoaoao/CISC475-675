//
//  Patient.swift
//  ReturnToSports
//
//  Created by Jia Ren on 4/23/17.
//  Copyright © 2017 Jia Ren. All rights reserved.
//

import os.log
import UIKit

class Patient: NSObject, NSCoding {
    // MARK: Properties
    var id: String?
    
    //MARK: Archiving Paths
    static let DocumentsDirectory = FileManager().urls(for: .documentDirectory, in: .userDomainMask).first!
    static let ArchiveURL = DocumentsDirectory.appendingPathComponent("patients")
    
    // MARK: Initialization
    init?(_ id: String) {
        self.id = id
    }
    
    //MARK: Types
    struct PropertyKey {
        static let id = "id"
    }

    // MARK: NSCoding
    func encode(with aCoder: NSCoder) {
        aCoder.encode(id, forKey: PropertyKey.id)
    }
    
    required convenience init?(coder aDecoder: NSCoder) {
        // The id is required. If we cannot decode a id string, the initializer should fail.
        guard let id = aDecoder.decodeObject(forKey: PropertyKey.id) as? String else {
            os_log("Unable to decode the id for a Patient object.", log: OSLog.default, type: .debug)
            return nil
        }
        // Must call designated initializer.
        self.init(id)
    }

}
