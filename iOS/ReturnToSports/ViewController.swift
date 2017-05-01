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
var questionnaireId: String = "1"

class ViewController: UIViewController, UITextFieldDelegate {
    // MARK: Properties:
    @IBOutlet weak var patientIdTextField: UITextField!
    @IBOutlet weak var surveyButton: UIButton!
    @IBOutlet weak var patientIdMissingLabel: UILabel!
    
    override func viewDidLoad() {
       
        super.viewDidLoad()
        
        patientIdTextField.delegate = self
        patientIdTextField.setBottomBorder()
        
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
            surveyButton.backgroundColor = UIColor.blue
            patientIdMissingLabel.text = " "
            // Create a new Pateint
            patient = Patient(id)
        }
        else {
            // print("patient id is empty")
            surveyButton.isEnabled = false
            surveyButton.backgroundColor = UIColor.lightGray
            patientIdMissingLabel.text = "! Patient id is required."
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


extension UITextField {
    func setBottomBorder() {
        self.borderStyle = .none
        self.layer.backgroundColor = UIColor.white.cgColor
        
        self.layer.masksToBounds = false
        self.layer.shadowColor = UIColor.gray.cgColor
        self.layer.shadowOffset = CGSize(width: 0.0, height: 0.5)
        self.layer.shadowOpacity = 1.0
        self.layer.shadowRadius = 0.0
    }
}
