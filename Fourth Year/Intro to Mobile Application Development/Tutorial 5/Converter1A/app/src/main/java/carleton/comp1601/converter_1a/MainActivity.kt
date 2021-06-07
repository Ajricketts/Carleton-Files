package carleton.comp1601.converter_1a

import android.os.Bundle
import android.text.Editable
import android.text.Html
import android.text.TextWatcher
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.text.HtmlCompat.fromHtml

class MainActivity : AppCompatActivity() {
    private lateinit var editTemperature: EditText
    private lateinit var editDistance: EditText
    private lateinit var TempResult: TextView
    private lateinit var result2: TextView
    private lateinit var DistResult: TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        TempResult = findViewById(R.id.TempResult)
        result2 = findViewById(R.id.result2)
        DistResult = findViewById(R.id.DistResult)
        editTemperature = findViewById(R.id.editTemperature)
        editDistance = findViewById(R.id.editDistance)
        editTemperature.addTextChangedListener(watcherTempature)
        editDistance.addTextChangedListener(watcherDistance)
    }
    private val watcherTempature = object : TextWatcher {
        override fun afterTextChanged(s: Editable) {
            val Fs = editTemperature.text.toString()
            var F = Fs.toDoubleOrNull()

            if (F == null) {
                TempResult.text = "Please enter a number to convert."
                result2.text = ""
            } else {
                val C = (F - 32.0) * (5.0 / 9.0)
                val K = C + 273.15
                val boldC = "<b>" + Fs + "</b>" + " Fahrenheit is " + "<b>" + String.format("%.4f Celcius", C) + "</b>"
                val boldK = "<b>" + Fs + "</b>" + " Fahrenheit is " + "<b>" + String.format("%.4f Celcius", K) + "</b>"
                TempResult.text = fromHtml(boldC,0)
                result2.text = fromHtml(boldK,0)
            }
        }

        override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
        }

        override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
        }
    }

    private val watcherDistance = object : TextWatcher {
        override fun afterTextChanged(s: Editable) {
            val Ms = editDistance.text.toString()
            var M = Ms.toDoubleOrNull()

            if (M == null) {
                DistResult.text = "Please enter a number to convert."
                result2.text = ""
            } else {
                val Kl = M * 1.60934
                val boldKl = "<b>" + M + "</b>" + " Miles is " + "<b>" + String.format("%.4f Kilometers", Kl) + "</b>"
                DistResult.text = fromHtml(boldKl,0)
            }
        }

        override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
        }

        override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
        }
    }
}
