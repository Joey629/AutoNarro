---
id: 'Date picker'
section: components
subsection: date-and-time
cssPrefix: pf-v6-c-date-picker
---import './DatePicker.css'

## Examples

### Basic

```html
<div class="pf-v6-c-date-picker">
  <div class="pf-v6-c-date-picker__input">
    <div class="pf-v6-c-input-group">
      <div class="pf-v6-c-input-group__item pf-m-fill">
        <span class="pf-v6-c-form-control">
          <input
            type="text"
            value="2020-03-05"
            id="basic-input"
            name="basic-input"
            aria-label="Date picker"
          />
        </span>
      </div>
      <div class="pf-v6-c-input-group__item">
        <button
          class="pf-v6-c-button pf-m-control"
          type="button"
          aria-label="Toggle date picker"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm320-196c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM192 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM64 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
</div>

```

### Helper text

```html
<div class="pf-v6-c-date-picker">
  <div class="pf-v6-c-date-picker__input">
    <div class="pf-v6-c-input-group">
      <div class="pf-v6-c-input-group__item pf-m-fill">
        <span class="pf-v6-c-form-control">
          <input
            type="text"
            value="2020-03-05"
            id="helper-text-input"
            name="helper-text-input"
            aria-label="Date picker"
          />
        </span>
      </div>
      <div class="pf-v6-c-input-group__item">
        <button
          class="pf-v6-c-button pf-m-control"
          type="button"
          aria-label="Toggle date picker"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm320-196c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM192 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM64 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-date-picker__helper-text">
    <div class="pf-v6-c-helper-text">
      <div class="pf-v6-c-helper-text__item">
        <span class="pf-v6-c-helper-text__item-text">Select a date</span>
      </div>
    </div>
  </div>
</div>

```

### Invalid

```html
<div class="pf-v6-c-date-picker">
  <div class="pf-v6-c-date-picker__input">
    <div class="pf-v6-c-input-group">
      <div class="pf-v6-c-input-group__item pf-m-fill">
        <span class="pf-v6-c-form-control pf-m-error">
          <input
            aria-invalid="true"
            type="text"
            value="2020-03-05"
            id="invalid-input"
            name="invalid-input"
            aria-label="Date picker"
          />
          <span class="pf-v6-c-form-control__utilities">
            <span class="pf-v6-c-form-control__icon pf-m-status">
              <i class="fas fa-exclamation-circle" aria-hidden="true"></i>
            </span>
          </span>
        </span>
      </div>
      <div class="pf-v6-c-input-group__item">
        <button
          class="pf-v6-c-button pf-m-control"
          type="button"
          aria-label="Toggle date picker"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm320-196c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM192 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM64 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-date-picker__helper-text">
    <div class="pf-v6-c-helper-text">
      <div class="pf-v6-c-helper-text__item pf-m-error">
        <span class="pf-v6-c-helper-text__item-icon">
          <i class="fas fa-fw fa-exclamation-circle" aria-hidden="true"></i>
        </span>
        <span class="pf-v6-c-helper-text__item-text">
          <span class="pf-v6-screen-reader">Error:</span>
          Invalid date
        </span>
      </div>
    </div>
  </div>
</div>

```

### Expanded

```html
<div class="pf-v6-c-date-picker">
  <div class="pf-v6-c-date-picker__input">
    <div class="pf-v6-c-input-group">
      <div class="pf-v6-c-input-group__item pf-m-fill">
        <span class="pf-v6-c-form-control">
          <input
            type="text"
            value="2020-03-05"
            id="expanded-input"
            name="expanded-input"
            aria-label="Date picker"
          />
        </span>
      </div>
      <div class="pf-v6-c-input-group__item">
        <button
          class="pf-v6-c-button pf-m-control"
          type="button"
          aria-label="Toggle date picker"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm320-196c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM192 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM64 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-date-picker__calendar">Calendar</div>
</div>

```

### Custom width input

```html
<div
  class="pf-v6-c-date-picker"
  style="--pf-v6-c-date-picker__input--c-form-control--Width: 220px;"
>
  <div class="pf-v6-c-date-picker__input">
    <div class="pf-v6-c-input-group">
      <div class="pf-v6-c-input-group__item pf-m-fill">
        <span class="pf-v6-c-form-control">
          <input
            type="text"
            value="November 20, 2020"
            id="custom-width-input-input"
            name="custom-width-input-input"
            aria-label="Date picker"
          />
        </span>
      </div>
      <div class="pf-v6-c-input-group__item">
        <button
          class="pf-v6-c-button pf-m-control"
          type="button"
          aria-label="Toggle date picker"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm320-196c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM192 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM64 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
</div>

```

### Custom width input based on number of characters

```html
<div
  class="pf-v6-c-date-picker"
  style="--pf-v6-c-date-picker__input--c-form-control--width-chars: 18;"
>
  <div class="pf-v6-c-date-picker__input">
    <div class="pf-v6-c-input-group">
      <div class="pf-v6-c-input-group__item pf-m-fill">
        <span class="pf-v6-c-form-control">
          <input
            type="text"
            value="November 20, 2020"
            id="custom-width-input-based-on-number-of-characters-input"
            name="custom-width-input-based-on-number-of-characters-input"
            aria-label="Date picker"
          />
        </span>
      </div>
      <div class="pf-v6-c-input-group__item">
        <button
          class="pf-v6-c-button pf-m-control"
          type="button"
          aria-label="Toggle date picker"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm320-196c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM192 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40zM64 268c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zm0 128c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H76c-6.6 0-12-5.4-12-12v-40zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
</div>

```

## Documentation

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-date-picker` | `<div>` | Initiates the date picker component. **Required** |
| `.pf-v6-c-date-picker__input` | `<div>` | Initiates the date picker input container. **Required** |
| `.pf-v6-c-date-picker__helper-text` | `<div>` | Initiates the date picker helper text. |
| `.pf-v6-c-date-picker__calendar` | `<div>` | Initiates an optional date picker calendar container. **Note:** Required in the react date picker component. |
| `.pf-m-top` | `.pf-v6-c-date-picker` | Modifies to display the calendar above the date picker. |
| `.pf-m-align-right` | `.pf-v6-c-date-picker__calendar` | Modifies the calendar to align the calendar to the right edge of the date picker. |
| `.pf-m-static` | `.pf-v6-c-date-picker__calendar` | Modifies the calendar to be statically positioned to support custom positioning. |
