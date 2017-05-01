//
//  WebViewController.swift
//  ReturnToSports
//
//  Created by Jia Ren on 4/4/17.
//  Copyright © 2017 Jia Ren. All rights reserved.
//

import UIKit
import WebKit

class WebViewController: UIViewController, WKNavigationDelegate {
    // MARK: Property
    var webView: WKWebView!
    var progressView: UIProgressView!

    let baseUrl = "http://127.0.0.1:8000/questionnaire"
    
    override func loadView() {
        webView = WKWebView()
        webView.navigationDelegate = self
        view = webView
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Clear Cache.
        if #available(iOS 9.0, *)
        {
            let websiteDataTypes = NSSet(array: [WKWebsiteDataTypeDiskCache, WKWebsiteDataTypeMemoryCache])
            let date = NSDate(timeIntervalSince1970: 0)
            
            WKWebsiteDataStore.default().removeData(ofTypes: websiteDataTypes as! Set<String>, modifiedSince: date as Date, completionHandler:{ })
        }
        else
        {
            var libraryPath = NSSearchPathForDirectoriesInDomains(FileManager.SearchPathDirectory.libraryDirectory, FileManager.SearchPathDomainMask.userDomainMask, false).first!
            libraryPath += "/Cookies"
            
            do {
                try FileManager.default.removeItem(atPath: libraryPath)
            } catch {
                print("error")
            }
            URLCache.shared.removeAllCachedResponses()
        }

        // Load survey page.
        if let pid = patient?.id {
            let surveyUrl = [baseUrl, questionnaireId, "patient_id", pid].joined(separator: "/") + "/"
            let url = URL(string: surveyUrl)!
            webView.load(URLRequest(url: url))
            webView.allowsBackForwardNavigationGestures = true
            webView.isUserInteractionEnabled = true
            
            progressView = UIProgressView(frame: CGRect(x: 0, y: 64, width: UIScreen.main.bounds.width, height: 75))
            webView.addSubview(progressView)
            progressView.isHidden = false
            
            webView.addObserver(self, forKeyPath: #keyPath(WKWebView.estimatedProgress), options: .new, context: nil)
        }
    }
    
    deinit { webView.removeObserver(self, forKeyPath: "estimatedProgress") }
    
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        title = webView.title
    }
    
    override func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {
        if keyPath == "estimatedProgress" {
            progressView.progress = Float(webView.estimatedProgress)
            if self.webView.estimatedProgress >= 1.0 {
                progressView.isHidden = true
            }
        }
    }
    
     override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
}

