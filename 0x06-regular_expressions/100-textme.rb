#!/usr/bin/env ruby

def extract_info(log_line)
  doc = REXML::Document.new(log_line) # Parse log line into XML document for easier parsing with XPath expressions
  sender = doc.root['from'] # Extract sender phone number or name using XPath expression to select 'from' attribute
  receiver = doc['message']['addresses']['address'][0]['address'] # Extract receiver phone number or name using XPath expression to select 'address' element inside 'addresses' element
  flags = doc['message']['flags'].split(':').map(&:to_i).compact # Extract flags using XPath expression to select 'flags' element and split by colon, then convert each element to integer and remove any empty strings
  [sender, receiver, flags.join(':')] # Return an array with sender, receiver, and flags
end

def main
  log_file = 'log_file.txt' # Path to log file
  regexp = /\A(Feb\s[0-9]{2}\s[0-9]{2}:[0-9]{2})\s(ip-\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3})\smdr:\s(20[0-9]{2}-[0-9]{2}-[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2})\s(Receive|Sent)\sSMS\s\[(SMSC|SYBASE[12])\]\s\[(SVC|backendtextme)\]\s\[(ACT|backendtextme|frontendtextme|textme)\]\s\[(BINF|textme)\]\s\[(FID|textme|frontendtextme|backendtextme)\]\s\[(from|to|Google|+[0-9]{10,12})\]\s\[(msg|text|This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.|Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended|Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.]\]\s\[(udh|text|0:]\)\s\z/i # Regular expression to match log line format

  results = [] # Array to store extracted information

  File.open(log_file, 'r') do |file| # Open log file for reading
    file.each_line do |line| # Iterate over each line in log file
      match = line.match(regexp) # Match log line against regular expression
      next unless match # Skip line if regular expression does not match
      results << extract_info(match[0]) # Extract information from matched line using `extract_info` method
    end
  end

  results.each do |result| # Print extracted information for each line
    puts result[0] + ', ' + result[1] + ', ' + result[2].join(':')
  end
end
