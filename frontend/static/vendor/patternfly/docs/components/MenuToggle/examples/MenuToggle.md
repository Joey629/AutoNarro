---
id: 'Menu toggle'
section: components
subsection: menus
cssPrefix: pf-v6-c-menu-toggle
---import './MenuToggle.css'

## Examples

### Collapsed

```html
<button class="pf-v6-c-menu-toggle" type="button" aria-expanded="false">
  <span class="pf-v6-c-menu-toggle__text">Collapsed</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Expanded

```html
<button
  class="pf-v6-c-menu-toggle pf-m-expanded"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__text">Expanded</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Disabled

```html
<button
  class="pf-v6-c-menu-toggle pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__text">Disabled</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Count

```html
<button class="pf-v6-c-menu-toggle" type="button" aria-expanded="false">
  <span class="pf-v6-c-menu-toggle__text">Count</span>
  <span class="pf-v6-c-menu-toggle__count">
    <span class="pf-v6-c-badge pf-m-unread">4 selected</span>
  </span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-text pf-m-small pf-m-plain"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__count">
    <span class="pf-v6-c-badge pf-m-unread">
      4
      <span class="pf-v6-screen-reader">additional items</span>
    </span>
  </span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Primary

```html
<button
  class="pf-v6-c-menu-toggle pf-m-primary"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Collapsed</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-primary"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-menu-toggle__text">Icon</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-primary"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__text">Expanded</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__text">Disabled</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Secondary

```html
<button
  class="pf-v6-c-menu-toggle pf-m-secondary"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Collapsed</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-secondary"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-menu-toggle__text">Icon</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-secondary"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__text">Expanded</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__text">Disabled</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Plain

```html
<button
  class="pf-v6-c-menu-toggle pf-m-plain"
  type="button"
  aria-expanded="false"
  aria-label="Actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-plain"
  type="button"
  aria-expanded="true"
  aria-label="Actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-plain pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
  aria-label="Actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>

```

### Plain circle

```html isBeta
<button
  class="pf-v6-c-menu-toggle pf-m-circle pf-m-plain"
  type="button"
  aria-expanded="false"
  aria-label="Circle styled actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-circle pf-m-expanded pf-m-plain"
  type="button"
  aria-expanded="true"
  aria-label="Circle and expanded styled actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-circle pf-m-plain pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
  aria-label="Circle and disabled styled actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>

```

### Plain with text

```html
<button
  class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Custom text</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-text pf-m-plain"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__text">Custom text</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-text pf-m-plain pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__text">Disabled</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Small

```html
<button
  class="pf-v6-c-menu-toggle pf-m-small"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Collapsed</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-small"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__text">Expanded</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-small pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__text">Disabled</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
<br />
<br />
<button
  class="pf-v6-c-menu-toggle pf-m-small pf-m-primary"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Collapsed</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-small pf-m-primary"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__text">Expanded</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-small pf-m-primary pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__text">Disabled</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
<br />
<br />
<button
  class="pf-v6-c-menu-toggle pf-m-small pf-m-secondary"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Collapsed</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-small pf-m-secondary"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__text">Expanded</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-small pf-m-secondary pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__text">Disabled</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
<br />
<br />
<button
  class="pf-v6-c-menu-toggle pf-m-text pf-m-small pf-m-plain"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Collapsed</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-text pf-m-small pf-m-plain"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__text">Expanded</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-text pf-m-small pf-m-plain pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__text">Disabled</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>
<br />
<br />
<button
  class="pf-v6-c-menu-toggle pf-m-small pf-m-plain"
  type="button"
  aria-expanded="false"
  aria-label="Actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-small pf-m-plain"
  type="button"
  aria-expanded="true"
  aria-label="Actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>
&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-small pf-m-plain pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
  aria-label="Actions"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
      />
    </svg>
  </span>
</button>

```

### With icon/image and text

```html
<button
  class="pf-v6-c-menu-toggle pf-m-secondary"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-menu-toggle__text">Icon</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
      />
    </svg>
  </span>
  <span class="pf-v6-c-menu-toggle__text">Icon</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### With avatar and text

```html
<button class="pf-v6-c-menu-toggle" type="button" aria-expanded="false">
  <span class="pf-v6-c-menu-toggle__icon">
    <img
      class="pf-v6-c-avatar pf-m-sm"
      alt="Avatar image"
      src="/assets/images/img_avatar-light.svg"
    />
  </span>
  <span class="pf-v6-c-menu-toggle__text">Ned Username</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-expanded"
  type="button"
  aria-expanded="true"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <img
      class="pf-v6-c-avatar pf-m-sm"
      alt="Avatar image"
      src="/assets/images/img_avatar-light.svg"
    />
  </span>
  <span class="pf-v6-c-menu-toggle__text">Ned Username</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

&nbsp;
<button
  class="pf-v6-c-menu-toggle pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
>
  <span class="pf-v6-c-menu-toggle__icon">
    <img
      class="pf-v6-c-avatar pf-m-sm"
      alt="Avatar image"
      src="/assets/images/img_avatar-light.svg"
    />
  </span>
  <span class="pf-v6-c-menu-toggle__text">Ned Username</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Full height

```html
<button
  class="pf-v6-c-menu-toggle pf-m-full-height"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Full height</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Full width

```html
<button
  class="pf-v6-c-menu-toggle pf-m-full-width"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Full width</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Form

```html
<button
  class="pf-v6-c-menu-toggle pf-m-form"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Select option</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Typeahead

```html
<div
  class="pf-v6-c-menu-toggle pf-m-full-width pf-m-typeahead"
  id="typeahead-example"
>
  <div class="pf-v6-c-text-input-group pf-m-plain">
    <div class="pf-v6-c-text-input-group__main">
      <span class="pf-v6-c-text-input-group__text">
        <input
          class="pf-v6-c-text-input-group__text-input"
          type="text"
          value
          aria-label="Type to filter"
        />
      </span>
    </div>
    <div class="pf-v6-c-text-input-group__utilities">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Clear input"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="typeahead-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

```

### Status

```html
<button
  class="pf-v6-c-menu-toggle pf-m-success"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Success</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__status-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

<br />
<br />

<button
  class="pf-v6-c-menu-toggle pf-m-warning"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Warning</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__status-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="m31.874 28.514-15.011-27a1.001 1.001 0 0 0-1.748 0l-15.011 27A1 1 0 0 0 .978 30H31a1 1 0 0 0 .874-1.486ZM14.5 12a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 26.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 26.001Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

<br />
<br />

<button
  class="pf-v6-c-menu-toggle pf-m-danger"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Danger</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__status-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Placeholder

```html
<button
  class="pf-v6-c-menu-toggle pf-m-placeholder"
  type="button"
  aria-expanded="false"
>
  <span class="pf-v6-c-menu-toggle__text">Placeholder text</span>
  <span class="pf-v6-c-menu-toggle__controls">
    <span class="pf-v6-c-menu-toggle__toggle-icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
        />
      </svg>
    </span>
  </span>
</button>

```

### Split toggle

Shown with default, primary, and secondary styling

```html
<div
  class="pf-v6-c-menu-toggle pf-m-split-button"
  id="split-button-checkbox-with-toggle-action-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button">Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-action-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-with-toggle-action-expanded-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button">Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-with-toggle-action-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-with-toggle-action-disabled-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button" disabled>Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-action-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button"
  id="split-button-checkbox-with-toggle-action-primary-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button">Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-action-primary-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-with-toggle-action-primary-expanded-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button">Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-with-toggle-action-primary-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-with-toggle-action-primary-disabled-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button" disabled>Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-action-primary-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button"
  id="split-button-checkbox-with-toggle-action-secondary-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button">Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-action-secondary-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-with-toggle-action-secondary-expanded-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button">Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-with-toggle-action-secondary-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-with-toggle-action-secondary-disabled-example"
>
  <button class="pf-v6-c-menu-toggle__button" type="button" disabled>Action</button>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-action-secondary-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

```

### Split toggle with checkbox

Shown with default, primary, and secondary styling

```html
<div
  class="pf-v6-c-menu-toggle pf-m-split-button"
  id="split-button-checkbox-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-example-input"
      name="split-button-checkbox-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-expanded-example-input"
      name="split-button-checkbox-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-checkbox-disabled-example-input"
      name="split-button-checkbox-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button"
  id="split-button-primary-checkbox-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-primary-checkbox-example-input"
      name="split-button-primary-checkbox-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-primary-checkbox-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-expanded pf-m-split-button"
  id="split-button--primary-checkbox-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button--primary-checkbox-expanded-example-input"
      name="split-button--primary-checkbox-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button--primary-checkbox-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button pf-m-disabled"
  id="split-button--primary-checkbox-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button--primary-checkbox-disabled-example-input"
      name="split-button--primary-checkbox-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button--primary-checkbox-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button"
  id="split-button-secondary-checkbox-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-secondary-checkbox-example-input"
      name="split-button-secondary-checkbox-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-secondary-checkbox-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-expanded pf-m-split-button"
  id="split-button-secondary-checkbox-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-secondary-checkbox-expanded-example-input"
      name="split-button-secondary-checkbox-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button-secondary-checkbox-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button pf-m-disabled"
  id="split-button-secondary-checkbox-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-secondary-checkbox-disabled-example-input"
      name="split-button-secondary-checkbox-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-secondary-checkbox-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

```

### Split toggle with labeled checkbox

To add a label to a split toggle that will be linked to the checkbox, pass the text wrapped in `span.pf-v6-c-check__label` as a child to `label.pf-v6-c-check`. Clicking the text will update the checked state of the split toggle's checkbox. <br/> <br/>
Shown with default, primary, and secondary styling

```html
<div
  class="pf-v6-c-menu-toggle pf-m-split-button"
  id="split-button-checkbox-with-toggle-text-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-with-toggle-text-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-with-toggle-text-example-input"
      name="split-button-checkbox-with-toggle-text-example-input"
    />
    <span class="pf-v6-c-check__label">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-text-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-with-toggle-text-expanded-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-with-toggle-text-expanded-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-with-toggle-text-expanded-example-input"
      name="split-button-checkbox-with-toggle-text-expanded-example-input"
    />
    <span class="pf-v6-c-check__label">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-with-toggle-text-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-with-toggle-text-disabled-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-with-toggle-text-disabled-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-checkbox-with-toggle-text-disabled-example-input"
      name="split-button-checkbox-with-toggle-text-disabled-example-input"
    />
    <span class="pf-v6-c-check__label pf-m-disabled">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-text-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button"
  id="split-button-checkbox-primary-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-primary-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-primary-example-input"
      name="split-button-checkbox-primary-example-input"
    />
    <span class="pf-v6-c-check__label">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-primary-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-primary-expanded-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-primary-expanded-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-primary-expanded-example-input"
      name="split-button-checkbox-primary-expanded-example-input"
    />
    <span class="pf-v6-c-check__label">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-primary-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-primary-disabled-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-primary-disabled-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-checkbox-primary-disabled-example-input"
      name="split-button-checkbox-primary-disabled-example-input"
    />
    <span class="pf-v6-c-check__label pf-m-disabled">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-primary-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button"
  id="split-button-checkbox-secondary-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-secondary-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-secondary-example-input"
      name="split-button-checkbox-secondary-example-input"
    />
    <span class="pf-v6-c-check__label">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-secondary-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-secondary-expanded-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-secondary-expanded-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-secondary-expanded-example-input"
      name="split-button-checkbox-secondary-expanded-example-input"
    />
    <span class="pf-v6-c-check__label">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-secondary-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>
&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-secondary-disabled-example"
>
  <label
    class="pf-v6-c-check"
    for="split-button-checkbox-secondary-disabled-example-input"
  >
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-checkbox-secondary-disabled-example-input"
      name="split-button-checkbox-secondary-disabled-example-input"
    />
    <span class="pf-v6-c-check__label pf-m-disabled">Select all items</span>
  </label>
  <button
    class="pf-v6-c-menu-toggle__button"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-secondary-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

```

### Split toggle with checkbox and toggle text

To add a label to a split toggle that will be linked to the toggle button, pass the text wrapped in `span.pf-v6-c-menu-toggle__text` as a child to `button.pf-v6-c-menu-toggle__button.pf-m-text`. Clicking the text should trigger any click action on the toggle. <br/> <br/>
Shown with default, primary, and secondary styling

```html
<div
  class="pf-v6-c-menu-toggle pf-m-split-button"
  id="split-button-checkbox-with-toggle-button-text-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-with-toggle-button-text-example-input"
      name="split-button-checkbox-with-toggle-button-text-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-button-text-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-with-toggle-button-text-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-with-toggle-button-text-expanded-example-input"
      name="split-button-checkbox-with-toggle-button-text-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-with-toggle-button-text-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-with-toggle-button-text-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-checkbox-with-toggle-button-text-disabled-example-input"
      name="split-button-checkbox-with-toggle-button-text-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-button-text-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button"
  id="split-button-primary-checkbox-with-toggle-button-text-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-primary-checkbox-with-toggle-button-text-example-input"
      name="split-button-primary-checkbox-with-toggle-button-text-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-primary-checkbox-with-toggle-button-text-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-expanded pf-m-split-button"
  id="split-button-primary-checkbox-with-toggle-button-text-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-primary-checkbox-with-toggle-button-text-expanded-example-input"
      name="split-button-primary-checkbox-with-toggle-button-text-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="true"
    id="split-button-primary-checkbox-with-toggle-button-text-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button pf-m-disabled"
  id="split-button-primary-checkbox-with-toggle-button-text-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-primary-checkbox-with-toggle-button-text-disabled-example-input"
      name="split-button-primary-checkbox-with-toggle-button-text-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-primary-checkbox-with-toggle-button-text-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button"
  id="split-button-secondary-checkbox-with-toggle-button-text-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-secondary-checkbox-with-toggle-button-text-example-input"
      name="split-button-secondary-checkbox-with-toggle-button-text-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-secondary-checkbox-with-toggle-button-text-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-expanded pf-m-split-button"
  id="split-button-secondary-checkbox-with-toggle-button-text-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-secondary-checkbox-with-toggle-button-text-expanded-example-input"
      name="split-button-secondary-checkbox-with-toggle-button-text-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="true"
    id="split-button-secondary-checkbox-with-toggle-button-text-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button pf-m-disabled"
  id="split-button-secondary-checkbox-with-toggle-button-text-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-secondary-checkbox-with-toggle-button-text-disabled-example-input"
      name="split-button-secondary-checkbox-with-toggle-button-text-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-secondary-checkbox-with-toggle-button-text-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__text">Toggle button text</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

```

### Split toggle with checkbox, icon, and toggle text

To add a label to a split toggle that will be linked to the toggle button, pass the text wrapped in `span.pf-v6-c-menu-toggle__text` as a child to `button.pf-v6-c-menu-toggle__button.pf-m-text`. Clicking the text should trigger any click action on the toggle. <br/> <br/>
Shown with default, primary, and secondary styling

```html
<div
  class="pf-v6-c-menu-toggle pf-m-split-button"
  id="split-button-checkbox-with-toggle-button-icon-text-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-with-toggle-button-icon-text-example-input"
      name="split-button-checkbox-with-toggle-button-icon-text-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-button-icon-text-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-expanded pf-m-split-button"
  id="split-button-checkbox-with-toggle-button-icon-text-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-checkbox-with-toggle-button-icon-text-expanded-example-input"
      name="split-button-checkbox-with-toggle-button-icon-text-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="true"
    id="split-button-checkbox-with-toggle-button-icon-text-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-split-button pf-m-disabled"
  id="split-button-checkbox-with-toggle-button-icon-text-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-checkbox-with-toggle-button-icon-text-disabled-example-input"
      name="split-button-checkbox-with-toggle-button-icon-text-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-checkbox-with-toggle-button-icon-text-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button"
  id="split-button-primary-checkbox-with-toggle-button-icon-text-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-primary-checkbox-with-toggle-button-icon-text-example-input"
      name="split-button-primary-checkbox-with-toggle-button-icon-text-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-primary-checkbox-with-toggle-button-icon-text-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-expanded pf-m-split-button"
  id="split-button-primary-checkbox-with-toggle-button-icon-text-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-primary-checkbox-with-toggle-button-icon-text-expanded-example-input"
      name="split-button-primary-checkbox-with-toggle-button-icon-text-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="true"
    id="split-button-primary-checkbox-with-toggle-button-icon-text-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-primary pf-m-split-button pf-m-disabled"
  id="split-button-primary-checkbox-with-toggle-button-icon-text-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-primary-checkbox-with-toggle-button-icon-text-disabled-example-input"
      name="split-button-primary-checkbox-with-toggle-button-icon-text-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-primary-checkbox-with-toggle-button-icon-text-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

<br />
<br />

<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button"
  id="split-button-secondary-checkbox-with-toggle-button-icon-text-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-secondary-checkbox-with-toggle-button-icon-text-example-input"
      name="split-button-secondary-checkbox-with-toggle-button-icon-text-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-secondary-checkbox-with-toggle-button-icon-text-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-expanded pf-m-split-button"
  id="split-button-secondary-checkbox-with-toggle-button-icon-text-expanded-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      id="split-button-secondary-checkbox-with-toggle-button-icon-text-expanded-example-input"
      name="split-button-secondary-checkbox-with-toggle-button-icon-text-expanded-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="true"
    id="split-button-secondary-checkbox-with-toggle-button-icon-text-expanded-example-toggle-button"
    aria-label="Menu toggle"
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>&nbsp;
<div
  class="pf-v6-c-menu-toggle pf-m-secondary pf-m-split-button pf-m-disabled"
  id="split-button-secondary-checkbox-with-toggle-button-icon-text-disabled-example"
>
  <label class="pf-v6-c-check pf-m-standalone">
    <input
      class="pf-v6-c-check__input"
      type="checkbox"
      disabled
      id="split-button-secondary-checkbox-with-toggle-button-icon-text-disabled-example-input"
      name="split-button-secondary-checkbox-with-toggle-button-icon-text-disabled-example-input"
      aria-label="Select all items"
    />
  </label>
  <button
    class="pf-v6-c-menu-toggle__button pf-m-text"
    type="button"
    aria-expanded="false"
    id="split-button-secondary-checkbox-with-toggle-button-icon-text-disabled-example-toggle-button"
    aria-label="Menu toggle"
    disabled
  >
    <span class="pf-v6-c-menu-toggle__icon">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 32 32"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
        />
      </svg>
    </span>
    <span class="pf-v6-c-menu-toggle__text">Icon</span>
    <span class="pf-v6-c-menu-toggle__controls">
      <span class="pf-v6-c-menu-toggle__toggle-icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
          />
        </svg>
      </span>
    </span>
  </button>
</div>

```

### Settings

```html
<button
  class="pf-v6-c-menu-toggle pf-m-settings pf-m-plain"
  type="button"
  aria-expanded="false"
  aria-label="Settings"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-menu-toggle pf-m-settings pf-m-expanded pf-m-plain"
  type="button"
  aria-expanded="true"
  aria-label="Settings"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
      />
    </svg>
  </span>
</button>

<button
  class="pf-v6-c-menu-toggle pf-m-settings pf-m-plain pf-m-disabled"
  type="button"
  aria-expanded="false"
  disabled
  aria-label="Settings"
>
  <span class="pf-v6-c-menu-toggle__icon">
    <svg
      class="pf-v6-svg"
      viewBox="0 0 32 32"
      fill="currentColor"
      aria-hidden="true"
      role="img"
      width="1em"
      height="1em"
    >
      <path
        d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
      />
    </svg>
  </span>
</button>

```

## Documentation

### Accessibility

| Class | Applied to | Outcome |
| -- | -- | -- |
| `aria-expanded="true"` | `.pf-v6-c-menu-toggle`, `.pf-v6-c-menu-toggle__button` | Indicates that the menu toggle component is in the expanded state. |
| `aria-expanded="false"` | `.pf-v6-c-menu-toggle`, `.pf-v6-c-menu-toggle__button` | Indicates that the menu toggle component is in the collapsed state. |
| `aria-label="Descriptive text"` | `.pf-v6-c-menu-toggle`, `.pf-v6-c-menu-toggle.pf-m-plain` | Gives the menu toggle component an accessible label. Used whenever there is no text visible in the menu toggle. Often, plain modifiers are used when the menu toggle only contains an icon. |
| `disabled` | `.pf-v6-c-menu-toggle`, `.pf-v6-c-menu-toggle__button` | Indicates that the menu toggle component is disabled. |

### Usage

| Class | Applied | Outcome |
| -- | -- | -- |
| `.pf-v6-c-menu-toggle` | `<button>` | Initiates the menu toggle component. |
| `.pf-v6-c-menu-toggle__icon` | `<span>` | Defines the menu toggle component icon/image. |
| `.pf-v6-c-menu-toggle__text` | `<span>` | Defines the menu toggle component text. |
| `.pf-v6-c-menu-toggle__count` | `<span>` | Defines the menu toggle component count. |
| `.pf-v6-c-menu-toggle__controls` | `<span>` | Defines the menu toggle component controls. |
| `.pf-v6-c-menu-toggle__toggle-icon` | `<span>` | Defines the menu toggle component toggle/arrow icon. |
| `.pf-v6-c-menu-toggle__button` | `<button>` | Initiates the menu toggle button. |
| `.pf-m-split-button` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the split button variation. |
| `.pf-m-text` | `.pf-v6-c-menu-toggle__button` | Modifies the menu toggle component split button variation with text. |
| `.pf-m-disabled` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the disabled variation. |
| `.pf-m-primary` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the primary variation. |
| `.pf-m-secondary` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the secondary variation. |
| `.pf-m-text` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the text variation. |
| `.pf-m-plain` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the plain variation. |
| `.pf-m-circle` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component to be circular in shape. This is intended to be applied only to a plain menu toggle without any text. |
| `.pf-m-expanded` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the expanded state. |
| `.pf-m-full-height` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component to full height of parent. |
| `.pf-m-full-width` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component to full width of parent. |
| `.pf-m-form` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle for use in forms with form element border radius. |
| `.pf-m-success` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the success state. |
| `.pf-m-warning` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the warning state. |
| `.pf-m-danger` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle component for the danger state. |
| `.pf-m-placeholder` | `.pf-v6-c-menu-toggle` | Modifies the menu toggle text for placeholder styles. |
| `.pf-m-text-expanded` | `.pf-v6-c-menu-toggle` | Modifies a dock menu toggle to show its text. |
