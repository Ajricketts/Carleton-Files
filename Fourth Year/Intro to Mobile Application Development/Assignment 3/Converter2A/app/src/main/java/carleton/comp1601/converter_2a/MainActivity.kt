package carleton.comp1601.converter_2a

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
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
    private var menuSelect: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d("Converter2A", "Created")

        menuButton = findViewById(R.id.convMenu)
        fromStringW = findViewById(R.id.fromString)
        result = findViewById(R.id.result)

        if (savedInstanceState != null) {
            with(savedInstanceState) {
                fromStringW.setText(getString("fromStringW"))
                menuSelect = getString("menuSelect").toString()
                val c = conversions[getString("menuSelect")]
                Log.d("Converter2A Restore", menuSelect)
                var from = fromStringW.text.toString().toDoubleOrNull()
                if (from != null) {
                    if (c != null) {
                        conv = c
                        result.setText(c.formatConversion(from))
                    }
                    else {
                        result.setText("Invalid menu selection")
                    }
                }
                else {
                    result.setText("Please enter a number to convert.")
                }
                fromStringW.setVisibility(View.VISIBLE)
                Log.d("TapDemo", "State restored")
            }
        }
        else {
            fromStringW.setVisibility(View.INVISIBLE)
        }
        fromStringW.addTextChangedListener(watcher)


    }

    fun onMenuItemClick(choice: MenuItem): Boolean {
        val convName = choice.getTitle()
        menuSelect = convName.toString()
        val c = conversions[menuSelect]
        Log.d("Converter2A Menu Click", menuSelect)

        if (c != null) {
            conv = c
            Log.d("Converter2A", "Converter Set")
            result.setText("You picked ${convName}")
            fromStringW.setText("")
            fromStringW.setVisibility(View.VISIBLE)
        } else {
            result.setText("Invalid Menu Selection")
            fromStringW.setVisibility(View.INVISIBLE)
        }
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

        override fun afterTextChanged(s: Editable) {
            val fromS = fromStringW.text.toString()
            var from = fromS.toDoubleOrNull()

            if (from == null) {
                result.setText("Please enter a number to convert.")
            } else {
                val c = conv

                if (c != null) {
                    result.setText(c.formatConversion(from))
                } else {
                    result.setText("No conversion selected.")
                }
            }

            Log.d("Converter2A Listener", menuSelect)

        }

        override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
        }

        override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        Log.d("Converter2A State save", menuSelect)

        outState.run {
            putString("fromStringW", fromStringW.text.toString())
            putString("menuSelect", menuSelect)
        }
        super.onSaveInstanceState(outState)

        Log.d("TapDemo", "State saved")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("Converter2A", "Destroyed")
    }

    override fun onResume() {
        super.onResume()
        Log.d("Converter2A", "Resumed")
    }

    override fun onPause() {
        super.onPause()
        Log.d("Converter2A", "Paused")
    }

    override fun onStart() {
        super.onStart()
        Log.d("Converter2A", "Started")
    }

    override fun onStop() {
        super.onStop()
        Log.d("Converter2A", "Stopped")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d("Converter2A", "Restarted")
    }
}
