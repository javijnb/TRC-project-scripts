#!/usr/bin/tclsh
set tcl_precision 17


proc Erlang {m a} {
    set a [expr $a + 0.0]
    for {set i 1; set B 1.0} {$i <= $m} {incr i} {
	set B [expr 1 + $i/$a*$B]
    }
    set B [expr 1/$B]
    return $B
}

set mEre(1) 0
set mEre(2) 0
set mEre(3) 0
set mEre(4) 0
set Ere(1) 0.0
set Ere(2) 0.0
set Ere(3) 0.0
set Ere(4) 0.0
proc ErlangRe {m a} {
    global mEre Ere
    if {$m > $mEre(3) || ($m < $mEre(2) && $m > 1) } {
	set minf [expr int(floor($m)-1.0)]
	if {$minf < 0} {set minf 0}
	foreach i {1 2 3 4} {
	    set mEre($i) $minf
	    set Ere($i) [expr log([Erlang $mEre($i) $a])]
	    set minf [expr $minf +1]
	}
    }
    set acum 0.0
    foreach i {4 3 2 1} {
	set factor 1.0
	set divisor 1
	foreach j {1 2 3 4} {
	    if {$i != $j} {
		set factor [expr $factor * ($m - $mEre($j))]
		set divisor [expr $divisor * ($mEre($i)-$mEre($j))]
	    }
	}
	set acum [expr $acum + $factor/$divisor * $Ere($i)]
    }
    return [expr exp($acum)]
}

proc alfanu {m a} {
    set B  [Erlang $m $a]
    set alpha [expr $a * $B]
    set nu [expr $alpha * (1-$alpha+$a/($m+1+$alpha-$a))]
    return "$alpha $nu"
}

proc alfanuRe {m a} {
    set B  [ErlangRe $m $a]
    set alpha [expr $a * $B]
    set nu [expr $alpha * (1-$alpha+$a/($m+1+$alpha-$a))]
    return "$alpha $nu"
}

proc pico {m A} {
    foreach {alfa nu} [alfanu $m $A] {}
    set r [expr $nu/$alfa]
    return $r
}

proc InvErlangRe {A B} {
    set b 1
    while {[Erlang $b $A] > $B} {incr b}
    set a [expr $b-1]
    set Eb [Erlang $b $A]
    set Ea [Erlang $a $A]
    set prevx 0
    while {1} {
	if {$b == $a} {
	    set x $a
	    break
	}
        set x [expr ($B-$Ea)*($b-$a)/($Eb-$Ea)+$a]
        set Ex [ErlangRe $x $A]
        #puts "\tE($x,$A)=$Ex $Eb $Ea $b $a"
        if {abs($prevx-$x)/$x < 1E-16} break
	set prevx $x
        if {$Ex > $B} {
            set b $x
            set Eb $Ex
        } else {
            set a $x
            set Ea $Ex
        }
    }
    return $x
}

proc InvErlangARe {m B} {
    set b [expr $m+0.0]
    while {[Erlang $m $b] < $B} {set b [expr $b*2]}
    set a [expr $b/2]
    while {[Erlang $m $a] > $B} {set a [expr $a/2]}
    set Eb [Erlang $m $b]
    set Ea [Erlang $m $a]
    set prevx 0
    while {1} {
        set x [expr ($B-$Ea)*($b-$a)/($Eb-$Ea)+$a]
        set Ex [Erlang $m $x]
        #puts "\tE($m,$x)=$Ex $prev $Eb $Ea $b $a"
        if {abs($prevx-$x)/$x < 1E-16} break
	set prevx $x
        if {$Ex > $B} {
            set b $x
            set Eb $Ex
        } else {
            set a $x
            set Ea $Ex
        }
    }
    return $x
}

proc uso {} { 
    global argv0
    puts "Uso Erlang directo: $argv0 <m> <A>"
    puts "Salida: B α ν"
    puts "Uso Erlang inverso en m: $argv0 -m <B> <A>"
    puts "Salida: m"
    puts "Uso Erlang inverso en A: $argv0 -A <B> <mℤ>"
    puts "Salida: A"
    puts "m,A,B  ℝ"
}

if {$argc != 2 && $argc != 3} {
    uso
    exit 2
}

if {$argc == 2} {
    foreach {m A} $argv {}
    if {! [string is double $m] ||  ![string is double $A]} {
	uso
	exit 3
    }
    
    if {[string is integer $m]} {
	set B [Erlang $m $A]
	set an [alfanu $m $A]
    } else {
	set B [ErlangRe $m $A]
	set an [alfanuRe $m $A]
    }
    puts "$B $an"
    exit 0
}

foreach {i B A} $argv {}

if {[string equal $i "-m"]} {
    if {! [string is double $B] || $B>=1 || $B <= 0 || ![string is double $A]} {
	uso
	exit 3
    }
    set m [InvErlangRe $A $B]
    puts $m
    exit 0
}

set m $A
if {[string equal $i "-A"]} {
    if {! [string is double $B] || $B>=1 || $B <= 0 || ![string is integer $m]} {
	uso
	exit 3
    }
    set A [InvErlangARe $m $B]
    puts $A
    exit 0
}



