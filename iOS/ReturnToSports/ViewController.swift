//
//  ViewController.swift
//  ReturnToSports
//
//  Created by Jia Ren on 4/4/17.
//  Copyright © 2017 Jia Ren. All rights reserved.
//

import UIKit

var patientId: String = "";
var questionnaireId: String = "2";

class ViewController: UIViewController {
    // MARK: Properties:
    @IBOutlet weak var patientIdTextField: UITextField!
    @IBOutlet weak var surveyButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        checkPatientId()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    /*
     // MARK: - Navigation
     
     // In a storyboard-based application, you will often want to do a little preparation before navigation
     override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
     // Get the new view controller using segue.destinationViewController.
     // Pass the selected object to the new view controller.
     }
     */
    
    // MARK: Action
    @IBAction func patientIdChange(_ sender: UITextField) {
        checkPatientId()
    }

    func checkPatientId() {
        if let id = patientIdTextField.text, !id.isEmpty {
            // print("patient id is entered")
            surveyButton.isEnabled = true
            patientId = id
        }
        else {
            // print("patient id is empty")
            surveyButton.isEnabled = false
        }
    }
}
