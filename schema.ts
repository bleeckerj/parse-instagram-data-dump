const artifactsCollection = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/artifacts' }),
  schema: z.object({
    contentMetadata: contentMetadata,
    entryDate: z.date(),
    updateDate: z.date().optional(),
    refDate: z.record(dateFromString, z.string()).optional(),
    references: z.array(z.string()).optional(),
    isDraft: z.boolean().default(true),
    description: z.string(),
    specifications: z.record(z.string(), z.string()).optional(),
    notes: z.array(z.string()).optional(),
    seo: z.string().optional(),
    coverImage: imageSchema,
    image: imageSchema,
    unfurlImage: imageSchema.optional(),
    imagesToGridDirectory: z.string().optional(),
    imageGridAltText: z.string().default("Image of the object"),
    imageGridSemanticKey: z.string().default("contentMetadata.name"),
    imagesFromGridDirectory: z.array(z.object({
      url: z.string(),
      altText: z.string().optional()
    })).optional(),
    images: z.array(imageSchema).optional(),
    tags: z.array(z.string()).optional(),
    urls: z.array(z.string().url()).optional(),
  })
});

const contentMetadata = z.object({
  title: z.string(),
  name: z.string(),
  customStyleTitle: z.string().optional(),
  indexPageStyleTitle: z.string().optional(),
  subtitle: z.string().optional(),
  identifier: z
    .string()
    .default('undefined-identifier')
    .refine((val) => val === undefined || noWhitespaceRegex.test(val), {
      message: "The string for 'identifier' must not contain any whitespace.",
    }),
  collectionName: z.string().optional(),
  titlesubtitle: z.string().optional(),
});

const dateFromString = z.string().transform((str) => new Date(str));


const imageSchema = z.object({
  url: z.string().default('https://nearfuturelaboratory.com/default-seo-image.webp'),
  caption: z.string().optional(),
  altText: z.string().default('Near Future Laboratory Design Fiction Imagine Harder')
});