package carleton.comp1601.picviewer2a

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.View
import android.widget.EditText
import android.widget.ImageView

val appName = "PicViewer2A"

class MainActivity : AppCompatActivity() {
    private lateinit var p: ImageView
    private var pic = R.drawable.kittens
    private lateinit var rotationInput: EditText
    private lateinit var scaleInput: EditText
    private lateinit var pXInput: EditText
    private lateinit var pYInput: EditText

    val Y = PicWatcher("Y", 0F, ::updateImage) {c -> if (c <= 1000) { c } else { 1000F }}
    val X = PicWatcher("X", 0F, ::updateImage) {c -> if (c >= -1000) { c } else { -1000F } }
    val rotation = PicWatcher("rotation", 0F, ::updateImage) {c -> if (c <= 720) { c } else { 720F }}
    val scale = PicWatcher("scale", 1F, ::updateImage) {c -> if (c in 0.0..5.0) { c } else { 1F }}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        p = findViewById(R.id.mypic)

        rotationInput = findViewById(R.id.rotation)
        rotationInput.setText(String.format("%.0f", 0F))
        rotationInput.addTextChangedListener(rotation)

        scaleInput = findViewById(R.id.scale)
        scaleInput.addTextChangedListener(scale)

        pXInput = findViewById(R.id.x)
        pXInput.addTextChangedListener(X)

        pYInput = findViewById(R.id.y)
        pYInput.addTextChangedListener(Y)

        if (savedInstanceState != null) {
            rotationInput.setText("rotation")
            scaleInput.setText("scale")
            pXInput.setText("X")
            pYInput.setText("Y")
            updateImage()
        }
        else{
            updateImage()
        }
        Log.d(appName, "Activity Created")
    }

    fun updateImage() {
        p.setImageResource(pic)
        p.setX(X.value)
        p.setY(Y.value)
        p.setRotation(rotation.value)
        p.setScaleX(scale.value)
        p.setScaleY(scale.value)
    }

    fun toggleImage(v: View) {
        if (pic == R.drawable.roshi) {
            pic = R.drawable.kittens
        } else {
            if (pic == R.drawable.kittens) {
                pic = R.drawable.fish
            }
            else {
                pic = R.drawable.roshi
            }
        }
        updateImage()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        outState.run {
            putString("X", X.value.toString())
            putString("Y", Y.value.toString())
            putString("rotation", rotation.value.toString())
            putString("scale", scale.value.toString())
        }
        super.onSaveInstanceState(outState)
        Log.d(appName, "State saved")
    }
}

class PicWatcher(n: String, v: Float, u: () -> Unit, c: (Float) -> Float): TextWatcher {
    var value: Float = v
    var name: String = n
    var update: () -> Unit = u
    var clamp: (Float) -> Float = c

    override fun afterTextChanged(s: Editable) {
        val new_value = s.toString().toFloatOrNull()

        if (new_value != null) {
            value = clamp(new_value)
            Log.d(appName, "Set ${name} to ${value} (wow).")
            update()
        }
        else {
            if (name!= "scale") {
                value = 0F
                Log.d(appName, "Set $name to $value.")
                update()
            }
            else {
                value = 1F
                Log.d(appName, "Set $name to $value.")
                update()
            }
        }
    }

    override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
    }

    override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
    }

}
