package carleton.comp1601.converter_2a

//  Conversions.kt

class Converter {
    var convFrom = "From Type"
    var convTo = "To Type"
    var convert: (from: Double) -> Double?

    fun formatConversion(from: Double): String {
        val to = this.convert(from)
        if (to != null) {
            return "${from} ${this.convFrom} is ${to} ${this.convTo}."
        } else {
            return "Converting ${from} ${convFrom} to ${this.convTo} failed."
        }
    }

    constructor(from: String, to: String, f: (from: Double) -> Double?) {
        this.convFrom = from
        this.convTo = to
        this.convert = f
    }
}

fun InToCM(inch: Double): Double? {
    val cm = 2.54 * inch
    return cm
}

val conversions = mapOf(
        "F to C" to Converter("Farenheit", "Celsius",
            {F ->  ((F - 32.0)*(5.0/9.0))}),
        "C to F" to Converter("Celsius","Farenheit",
            {((9.0/5.0)*it + 32.0)}),
        "km to mi" to Converter("kilometers", "miles",
            fun (k: Double): Double? {
                val m = k * 0.6213712
                return m
            }),
        "inch to cm" to Converter("inches", "centimeters", ::InToCM),
        "F to K" to Converter("Farenheit", "Kelvin",
            fun (F: Double): Double? {
                val kel = (F - 32.0) * 5.0/9.0 + 273.15
                if (kel > 0) {
                    return kel
                }
                else return null
            }),
        "cars to cows" to null
)

