package carleton.comp1601.tapdemo

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log
import android.view.View
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private lateinit var myMessage: TextView
    private var count = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d("TapDemo", "Created")

        myMessage = findViewById(R.id.myMessage)

        if (savedInstanceState != null) {
            with(savedInstanceState) {
                count = getInt("count")
                Log.d("TapDemo", "State restored")
            }
        } else {
            count = 0
        }

        myMessageSet()
    }

    @SuppressLint("SetTextI18n")
    fun myMessageSet() {
        if (count > 0) {
            myMessage.text = "You clicked $count times."
        }
        else {
            myMessage.text = "You havent clicked yet"
        }
    }

    @SuppressLint("SetTextI18n")
    fun myButtonPressed(v: View) {
        count++
        myMessageSet()

        Log.d("TapDemo", "Button Pressed")
    }

    override fun onSaveInstanceState(outState: Bundle) {
        outState.run {
            putInt("count", count)
        }
        super.onSaveInstanceState(outState)

        Log.d("TapDemo", "State saved")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("TapDemo", "Destroyed")
    }

    override fun onResume() {
        super.onResume()
        Log.d("TapDemo", "Resumed")
    }

    override fun onPause() {
        super.onPause()
        Log.d("TapDemo", "Paused")
    }

    override fun onStart() {
        super.onStart()
        Log.d("TapDemo", "Started")
    }

    override fun onStop() {
        super.onStop()
        Log.d("TapDemo", "Stopped")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d("TapDemo", "Restarted")
    }
}