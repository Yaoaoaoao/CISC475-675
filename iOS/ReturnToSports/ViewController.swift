//
//  ViewController.swift
//  ReturnToSports
//
//  Created by Jia Ren on 4/4/17.
//  Copyright © 2017 Jia Ren. All rights reserved.
//

import UIKit
import os.log

var patient: Patient?
var questionnaireId: String = "2"

class ViewController: UIViewController, UITextFieldDelegate {
    // MARK: Properties:
    @IBOutlet weak var patientIdTextField: UITextField!
    @IBOutlet weak var surveyButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        patientIdTextField.delegate = self
        
        // Load any saved patient.
        if let savedPatient = loadPatient() {
            os_log("Patient loaded.", log: OSLog.default, type: .debug)
            patientIdTextField.text = savedPatient.id
            patient = savedPatient
        }
        else {
            patientIdTextField.text = ""
        }
        
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
    
    @IBAction func patientIdChangeDone(_ sender: UITextField) {
        savePatient()
    }

    @IBAction func textFieldPrimaryActionTriggered(_ sender: Any) {
        checkPatientId()
        savePatient()
    }
    
    func checkPatientId() {
        if let id = patientIdTextField.text, !id.isEmpty {
            // print("patient id is entered")
            surveyButton.isEnabled = true
            // Create a new Pateint
            patient = Patient(id)
        }
        else {
            // print("patient id is empty")
            surveyButton.isEnabled = false
            patient = Patient("")
        }
    }
    
    // MARK: Private Methods
    private func savePatient() {
        let isSuccessfulSave = NSKeyedArchiver.archiveRootObject(patient!, toFile: Patient.ArchiveURL.path)
            if isSuccessfulSave {
                os_log("Patient successfully saved.", log: OSLog.default, type: .debug)
            } else {
                os_log("Failed to save patient...", log: OSLog.default, type: .error)
            }
    }
    
    private func loadPatient() -> Patient?  {
        return NSKeyedUnarchiver.unarchiveObject(withFile: Patient.ArchiveURL.path) as? Patient
    }
}
