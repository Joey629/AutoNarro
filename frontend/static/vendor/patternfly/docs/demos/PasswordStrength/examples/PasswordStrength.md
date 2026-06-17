---
id: 'Password strength'
section: components
---## Examples

### Initial state

```html
<form class="pf-v6-c-form" novalidate>
  <div class="pf-v6-c-form__group">
    <div class="pf-v6-c-form__group-label pf-m-info">
      <div class="pf-v6-c-form__group-label-main"><label
          class="pf-v6-c-form__label"
          for="password-strength-demo--initial-password"
        >
          <span class="pf-v6-c-form__label-text">Password</span>&nbsp;<span class="pf-v6-c-form__label-required" aria-hidden="true">&#42;</span></label>
      </div>
      <div class="pf-v6-c-form__group-label-info"></div>
    </div>
    <div class="pf-v6-c-form__group-control">
      <div class="pf-v6-c-input-group">
        <div class="pf-v6-c-input-group__item pf-m-fill">
          <span class="pf-v6-c-form-control pf-m-required">
            <input
              required
              type="text"
              id="password-strength-demo--initial-password"
              name="password-strength-demo--initial-password"
              aria-label="Password input"
              value
              placeholder="Password"
            />
          </span>
        </div>
        <div class="pf-v6-c-input-group__item">
          <button
            class="pf-v6-c-button pf-m-control"
            type="button"
            aria-label="Show password"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 640 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M320 400c-75.85 0-137.25-58.71-142.9-133.11L72.2 185.82c-13.79 17.3-26.48 35.59-36.72 55.59a32.35 32.35 0 0 0 0 29.19C89.71 376.41 197.07 448 320 448c26.91 0 52.87-4 77.89-10.46L346 397.39a144.13 144.13 0 0 1-26 2.61zm313.82 58.1l-110.55-85.44a331.25 331.25 0 0 0 81.25-102.07 32.35 32.35 0 0 0 0-29.19C550.29 135.59 442.93 64 320 64a308.15 308.15 0 0 0-147.32 37.7L45.46 3.37A16 16 0 0 0 23 6.18L3.37 31.45A16 16 0 0 0 6.18 53.9l588.36 454.73a16 16 0 0 0 22.46-2.81l19.64-25.27a16 16 0 0 0-2.82-22.45zm-183.72-142l-39.3-30.38A94.75 94.75 0 0 0 416 256a94.76 94.76 0 0 0-121.31-92.21A47.65 47.65 0 0 1 304 192a46.64 46.64 0 0 1-1.54 10l-73.61-56.89A142.31 142.31 0 0 1 320 112a143.92 143.92 0 0 1 144 144c0 21.63-5.29 41.79-13.9 60.11z"
                />
              </svg>
            </span>
          </button>
        </div>
      </div>
      <div class="pf-v6-c-form__helper-text" aria-live="polite">
        <div class="pf-v6-c-helper-text">
          <div
            class="pf-v6-c-helper-text__item pf-m-indeterminate pf-m-dynamic"
          >
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-minus" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Indeterminate:</span>
              Must be at least 14 characters
            </span>
          </div>
          <div
            class="pf-v6-c-helper-text__item pf-m-indeterminate pf-m-dynamic"
          >
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-minus" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Indeterminate:</span>
              Cannot contain the word "redhat"
            </span>
          </div>
          <div
            class="pf-v6-c-helper-text__item pf-m-indeterminate pf-m-dynamic"
          >
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-minus" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Indeterminate:</span>
              Must include at least 3 of the following: lowercase letters, uppercase letters, numbers, symbols
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</form>

```

### Invalid password

```html
<form class="pf-v6-c-form" novalidate>
  <div class="pf-v6-c-form__group">
    <div class="pf-v6-c-form__group-label pf-m-info">
      <div class="pf-v6-c-form__group-label-main"><label
          class="pf-v6-c-form__label"
          for="password-strength-demo--invalid-password"
        >
          <span class="pf-v6-c-form__label-text">Password</span>&nbsp;<span class="pf-v6-c-form__label-required" aria-hidden="true">&#42;</span></label>
      </div>
      <div class="pf-v6-c-form__group-label-info"></div>
    </div>
    <div class="pf-v6-c-form__group-control">
      <div class="pf-v6-c-input-group">
        <div class="pf-v6-c-input-group__item pf-m-fill">
          <span class="pf-v6-c-form-control pf-m-required">
            <input
              required
              type="text"
              id="password-strength-demo--invalid-password"
              name="password-strength-demo--invalid-password"
              aria-label="Password input"
              value="Marie$RedHat78"
              placeholder="Password"
            />
          </span>
        </div>
        <div class="pf-v6-c-input-group__item">
          <button
            class="pf-v6-c-button pf-m-control"
            type="button"
            aria-label="Show password"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 640 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M320 400c-75.85 0-137.25-58.71-142.9-133.11L72.2 185.82c-13.79 17.3-26.48 35.59-36.72 55.59a32.35 32.35 0 0 0 0 29.19C89.71 376.41 197.07 448 320 448c26.91 0 52.87-4 77.89-10.46L346 397.39a144.13 144.13 0 0 1-26 2.61zm313.82 58.1l-110.55-85.44a331.25 331.25 0 0 0 81.25-102.07 32.35 32.35 0 0 0 0-29.19C550.29 135.59 442.93 64 320 64a308.15 308.15 0 0 0-147.32 37.7L45.46 3.37A16 16 0 0 0 23 6.18L3.37 31.45A16 16 0 0 0 6.18 53.9l588.36 454.73a16 16 0 0 0 22.46-2.81l19.64-25.27a16 16 0 0 0-2.82-22.45zm-183.72-142l-39.3-30.38A94.75 94.75 0 0 0 416 256a94.76 94.76 0 0 0-121.31-92.21A47.65 47.65 0 0 1 304 192a46.64 46.64 0 0 1-1.54 10l-73.61-56.89A142.31 142.31 0 0 1 320 112a143.92 143.92 0 0 1 144 144c0 21.63-5.29 41.79-13.9 60.11z"
                />
              </svg>
            </span>
          </button>
        </div>
      </div>
      <div class="pf-v6-c-form__helper-text" aria-live="polite">
        <div class="pf-v6-c-helper-text">
          <div class="pf-v6-c-helper-text__item pf-m-success pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Must be at least 14 characters
            </span>
          </div>
          <div class="pf-v6-c-helper-text__item pf-m-error pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-exclamation-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Error:</span>
              Cannot contain the word "redhat"
            </span>
          </div>
          <div class="pf-v6-c-helper-text__item pf-m-success pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Must include at least 3 of the following: lowercase letters, uppercase letters, numbers, symbols
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</form>

```

### Valid, weak password

```html
<form class="pf-v6-c-form" novalidate>
  <div class="pf-v6-c-form__group">
    <div class="pf-v6-c-form__group-label pf-m-info">
      <div class="pf-v6-c-form__group-label-main"><label
          class="pf-v6-c-form__label"
          for="password-strength-demo--weak-password"
        >
          <span class="pf-v6-c-form__label-text">Password</span>&nbsp;<span class="pf-v6-c-form__label-required" aria-hidden="true">&#42;</span></label>
      </div>
      <div class="pf-v6-c-form__group-label-info">
        <div class="pf-v6-c-helper-text">
          <div class="pf-v6-c-helper-text__item pf-m-error">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-exclamation-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Error:</span>
              Weak
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-form__group-control">
      <div class="pf-v6-c-input-group">
        <div class="pf-v6-c-input-group__item pf-m-fill">
          <span class="pf-v6-c-form-control pf-m-required">
            <input
              required
              type="text"
              id="password-strength-demo--weak-password"
              name="password-strength-demo--weak-password"
              aria-label="Password input"
              value="Marie$Can3Read"
              placeholder="Password"
            />
          </span>
        </div>
        <div class="pf-v6-c-input-group__item">
          <button
            class="pf-v6-c-button pf-m-control"
            type="button"
            aria-label="Show password"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 640 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M320 400c-75.85 0-137.25-58.71-142.9-133.11L72.2 185.82c-13.79 17.3-26.48 35.59-36.72 55.59a32.35 32.35 0 0 0 0 29.19C89.71 376.41 197.07 448 320 448c26.91 0 52.87-4 77.89-10.46L346 397.39a144.13 144.13 0 0 1-26 2.61zm313.82 58.1l-110.55-85.44a331.25 331.25 0 0 0 81.25-102.07 32.35 32.35 0 0 0 0-29.19C550.29 135.59 442.93 64 320 64a308.15 308.15 0 0 0-147.32 37.7L45.46 3.37A16 16 0 0 0 23 6.18L3.37 31.45A16 16 0 0 0 6.18 53.9l588.36 454.73a16 16 0 0 0 22.46-2.81l19.64-25.27a16 16 0 0 0-2.82-22.45zm-183.72-142l-39.3-30.38A94.75 94.75 0 0 0 416 256a94.76 94.76 0 0 0-121.31-92.21A47.65 47.65 0 0 1 304 192a46.64 46.64 0 0 1-1.54 10l-73.61-56.89A142.31 142.31 0 0 1 320 112a143.92 143.92 0 0 1 144 144c0 21.63-5.29 41.79-13.9 60.11z"
                />
              </svg>
            </span>
          </button>
        </div>
      </div>
      <div class="pf-v6-c-form__helper-text" aria-live="polite">
        <div class="pf-v6-c-helper-text">
          <div class="pf-v6-c-helper-text__item pf-m-success pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Must be at least 14 characters
            </span>
          </div>
          <div class="pf-v6-c-helper-text__item pf-m-success pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Cannot contain the word "redhat"
            </span>
          </div>
          <div class="pf-v6-c-helper-text__item pf-m-success pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Must include at least 3 of the following: lowercase letters, uppercase letters, numbers, symbols
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</form>

```

### Valid, strong password

```html
<form class="pf-v6-c-form" novalidate>
  <div class="pf-v6-c-form__group">
    <div class="pf-v6-c-form__group-label pf-m-info">
      <div class="pf-v6-c-form__group-label-main"><label
          class="pf-v6-c-form__label"
          for="password-strength-demo--strong-password"
        >
          <span class="pf-v6-c-form__label-text">Password</span>&nbsp;<span class="pf-v6-c-form__label-required" aria-hidden="true">&#42;</span></label>
      </div>
      <div class="pf-v6-c-form__group-label-info">
        <div class="pf-v6-c-helper-text">
          <div class="pf-v6-c-helper-text__item pf-m-success">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Strong
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-form__group-control">
      <div class="pf-v6-c-input-group">
        <div class="pf-v6-c-input-group__item pf-m-fill">
          <span class="pf-v6-c-form-control pf-m-required">
            <input
              required
              type="text"
              id="password-strength-demo--strong-password"
              name="password-strength-demo--strong-password"
              aria-label="Password input"
              value="Marie$Can8Read3Pass@Word"
              placeholder="Password"
            />
          </span>
        </div>
        <div class="pf-v6-c-input-group__item">
          <button
            class="pf-v6-c-button pf-m-control"
            type="button"
            aria-label="Show password"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 640 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M320 400c-75.85 0-137.25-58.71-142.9-133.11L72.2 185.82c-13.79 17.3-26.48 35.59-36.72 55.59a32.35 32.35 0 0 0 0 29.19C89.71 376.41 197.07 448 320 448c26.91 0 52.87-4 77.89-10.46L346 397.39a144.13 144.13 0 0 1-26 2.61zm313.82 58.1l-110.55-85.44a331.25 331.25 0 0 0 81.25-102.07 32.35 32.35 0 0 0 0-29.19C550.29 135.59 442.93 64 320 64a308.15 308.15 0 0 0-147.32 37.7L45.46 3.37A16 16 0 0 0 23 6.18L3.37 31.45A16 16 0 0 0 6.18 53.9l588.36 454.73a16 16 0 0 0 22.46-2.81l19.64-25.27a16 16 0 0 0-2.82-22.45zm-183.72-142l-39.3-30.38A94.75 94.75 0 0 0 416 256a94.76 94.76 0 0 0-121.31-92.21A47.65 47.65 0 0 1 304 192a46.64 46.64 0 0 1-1.54 10l-73.61-56.89A142.31 142.31 0 0 1 320 112a143.92 143.92 0 0 1 144 144c0 21.63-5.29 41.79-13.9 60.11z"
                />
              </svg>
            </span>
          </button>
        </div>
      </div>
      <div class="pf-v6-c-form__helper-text" aria-live="polite">
        <div class="pf-v6-c-helper-text">
          <div class="pf-v6-c-helper-text__item pf-m-success pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Must be at least 14 characters
            </span>
          </div>
          <div class="pf-v6-c-helper-text__item pf-m-success pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Cannot contain the word "redhat"
            </span>
          </div>
          <div class="pf-v6-c-helper-text__item pf-m-success pf-m-dynamic">
            <span class="pf-v6-c-helper-text__item-icon">
              <i class="fas fa-fw fa-check-circle" aria-hidden="true"></i>
            </span>
            <span class="pf-v6-c-helper-text__item-text">
              <span class="pf-v6-screen-reader">Success:</span>
              Must include at least 3 of the following: lowercase letters, uppercase letters, numbers, symbols
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</form>

```

## Documentation

This demo implements a password strength meter. It uses multiple helper text items in the form helper text area below the input field to indicate whether the password meets validity criteria. Once the validity criteria are met, it also places helper text in the info area above the input field to indicate the strength of the password.
