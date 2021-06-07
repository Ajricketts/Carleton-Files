package carleton.comp1601.converter_2a

import android.annotation.SuppressLint
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.MenuItem
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.PopupMenu

class MainActivity : AppCompatActivity() {
    private lateinit var result: TextView
    private lateinit var menuButton: Button
    private lateinit var fromStringW: EditText
    private var conv: Converter? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        menuButton = findViewById(R.id.convMenu)
        fromStringW = findViewById(R.id.fromString)
        result = findViewById(R.id.result)

        fromStringW.addTextChangedListener(watcher)
        fromStringW.visibility = View.INVISIBLE
    }

    @SuppressLint("SetTextI18n")
    fun onMenuItemClick(choice: MenuItem): Boolean {
        val convName = choice.title
        val c = conversions[convName]

        if (c != null) {
            conv = c
            fromStringW.setText("")
            result.text = "You picked $convName"
        } else {
            result.text = "Invalid Menu Selection"
        }

        fromStringW.visibility = View.VISIBLE
        return true
    }

    // https://stackoverflow.com/questions/15580111/
    fun showMenu(v: View) {
        val menu = PopupMenu(this, v)

        for (s in conversions.keys) {
            menu.menu.add(s)
        }

        menu.setOnMenuItemClickListener(::onMenuItemClick)
        menu.show()
    }

    private val watcher = object : TextWatcher {

        @SuppressLint("SetTextI18n")
        override fun afterTextChanged(s: Editable) {
            val fromS = fromStringW.text.toString()
            var from = fromS.toDoubleOrNull()

            if (from == null) {
                result.text = "Please enter a number to convert."
            } else {
                val c = conv

                if (c != null) {
                    result.text = c.formatConversion(from)
                } else {
                    result.text = "No conversion selected."
                }
            }
        }

        override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
        }

        override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
        }
    }
}
