#!/usr/bin/env ruby
require 'oniguruma'

def match_school(input)
  Oniguruma::Regexp.new("School").match(input)
end

if ARGV.empty?
  puts "Please provide an argument"
else
  result = match_school(ARGV[0])
  if result
    puts "Match found: #{result.begin(0)} - #{result.end(0)}"
  else
    puts "No match found"
  end
end

